from twiter import app, db
from twiter import Users, Twit
from flask import request, jsonify, session, url_for
from datetime import datetime
from sqlalchemy import text

# 11. Get User profile, utama
@app.route('/profile', methods=['GET'])
def user_profile():
    # json 'username'
    try:
        data = request.get_json()
        # Mendapatkan data dari request
        username = data.get('username')
        # Memeriksa apakah user dengan username yang diberikan ada dalam database
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return jsonify({'message': 'User tidak ditemukan'}), 404
        profile_data = {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'birth_date': user.birth_date,
                    'twit_count': len(user.twits),
                    'following_count': len(user.following),
                    'followers_count': len(user.followers)
                }
        return jsonify(profile_data), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mengambil profil pengguna', 'error': str(e)}), 500

# 12. Follow a User, utama
@app.route('/follow', methods=['POST'])
def follow_user():
    # json 'username'
    try:
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum login, silakan login terlebih dahulu'}), 401
        follower_id = int(session['user_id'])  # Mengonversi follower_id menjadi integer
        #  mendapatkan username
        data = request.get_json()
        username = data.get('username')
        # Mengambil pengguna yang diikuti dan pengikut dari database
        followed_user = Users.query.filter_by(username=username).first()
        follower_user = Users.query.get(follower_id)
        # Memastikan pengguna yang diikuti dan pengikutnya ada di database
        if followed_user is None or follower_user is None:
            return jsonify({'message': 'User tidak ditemukan!'}), 404
        # Memastikan pengguna tidak mengikuti dirinya sendiri
        if followed_user == follower_user:
            return jsonify({'message': 'Tidak dapat mengikuti diri sendiri!'}), 400
        # Memastikan pengikut tidak mengikuti pengguna yang sama lagi
        if followed_user in follower_user.following:
            return jsonify({'message': f'Anda sudah mengikuti {followed_user.username}!'}), 400
        # Menambahkan pengguna yang diikuti ke daftar pengikut
        follower_user.following.append(followed_user)
        # Update aktivitas pengguna
        follower_user.last_activate = datetime.now().date()
        follower_user.last_activity = f'mengikuti akun {username}'
        db.session.commit()
        return jsonify({'message': f'Berhasil mengikuti {followed_user.username}!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat following user', 'error': str(e)}), 500

# 13. Unfollow a User, utama
@app.route('/unfollow', methods=['DELETE'])
def unfollow_user():
    # json 'username'
    try:
        if 'user_id' not in session:
            return {
            'message': 'Kamu belum login, silahkan melakukan login'
            }
        follower_id = int(session['user_id'])
        # Memeriksa apakah pengguna yang sedang login sudah mem-follow pengguna yang akan di-unfollow
        follower = Users.query.get(follower_id)
        # mendapatkan username
        data = request.get_json()
        username = data.get('username')
        user_to_unfollow = Users.query.filter_by(username=username).first()
        if not user_to_unfollow or user_to_unfollow not in follower.following:
            return jsonify({'message': f'Anda belum mengikuti {username}'}), 400
        # Menghapus relasi follow antara pengguna yang sedang login dengan pengguna yang akan di-unfollow
        follower.following.remove(user_to_unfollow)
        # Update aktivitas terakhir pengguna yang sedang login
        follower.last_activate = datetime.now().date()
        follower.last_activity = f'berhenti mengikuti akun {username}'
        db.session.commit()
        return jsonify({'message': 'Berhenti mengikuti berhasil'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat berhenti mengikuti pengguna', 'error': str(e)}), 500

# 14. Get follower from a User, utama
@app.route('/followers', methods=['GET'])
def user_followers():
    # json 'username', 'page'
    try:
        # mendapatkan username
        data = request.get_json()
        username = data.get('username')
        # Memeriksa apakah pengguna dengan nama pengguna yang diberikan ada dalam database
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return jsonify({'message': 'Pengguna tidak ditemukan'}), 404
        # Query langsung untuk mendapatkan daftar pengguna yang mengikuti pengguna dengan nama pengguna yang diberikan
        query = text(f"""
            SELECT u.username, u.first_name, u.last_name
            FROM users u
                INNER JOIN user_follows uf 
                ON u.id = uf.follower_id
            WHERE uf.followed_id = (SELECT id FROM users WHERE username = '{username}')
            ORDER BY u.username
            LIMIT :limit
            OFFSET :offset;
        """)
        # Mendapatkan parameter paginasi
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        # Eksekusi query dengan parameter paginasi
        followers = db.session.execute(query, {'limit': per_page, 'offset': offset})
        # Memuat data pengguna ke dalam format yang sesuai
        followers_list = [{
            'username': follower.username,
            'first_name': follower.first_name,
            'last_name': follower.last_name
        } for follower in followers]
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = url_for('user_followers', username=username, page=page + 1, _external=True)
        return jsonify({'followers': followers_list, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengikut', 'error': str(e)}), 500
      
# 15. Get user following, utama
@app.route('/followed', methods=['GET'])
def user_followed():
    # json 'username', 'page'
    try:
        # mendapatkan username
        data = request.get_json()
        username = data.get('username')
        # Memeriksa apakah pengguna dengan nama pengguna yang diberikan ada dalam database
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return jsonify({'message': 'Pengguna tidak ditemukan'}), 404
        # Query langsung untuk mendapatkan daftar pengguna yang diikuti oleh pengguna dengan nama pengguna yang diberikan
        query = text(f"""
            SELECT u.username, u.first_name, u.last_name
            FROM users u
                INNER JOIN user_follows uf 
                ON u.id = uf.followed_id
            WHERE uf.follower_id = (SELECT id FROM users WHERE username = '{username}')
            LIMIT :limit
            OFFSET :offset;
        """)
        # Mendapatkan parameter paginasi
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        # Eksekusi query dengan parameter paginasi
        followed_users = db.session.execute(query, {'limit': per_page, 'offset': offset})
        # Memuat data pengguna ke dalam format yang sesuai
        followed_list = [{
            'username': followed_user.username,
            'first_name': followed_user.first_name,
            'last_name': followed_user.last_name
        } for followed_user in followed_users]
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = url_for('user_followed', username=username, page=page + 1, _external=True)
        return jsonify({'followed': followed_list, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengguna yang diikuti', 'error': str(e)}), 500


# 16. list tweet, utama
@app.route('/twit', methods=['GET'])
def user_twit():
    # json 'username', 'page'
    try:
        # mendapatkan username
        data = request.get_json()
        username = data.get('username')
        # Memeriksa apakah pengguna dengan nama pengguna yang diberikan ada dalam database
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return jsonify({'message': 'Pengguna tidak ditemukan'}), 404
        # Query langsung untuk mendapatkan daftar twit dari pengguna dengan nama pengguna yang diberikan
        query = text(f"""
            SELECT t.id, u.username, t.twit_text, t.date_post, COUNT(l.user_id) AS likes
            FROM twit t
                JOIN users u 
                ON t.user_id = u.id
                LEFT JOIN "like" l
                ON t.id = l.twit_id
            WHERE u.username = '{username}'
            GROUP BY t.id, u.username
            ORDER BY t.date_post DESC
            LIMIT :limit
            OFFSET :offset;
        """)
        # Mendapatkan parameter paginasi
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        # Eksekusi query dengan parameter paginasi
        twits = db.session.execute(query, {'limit': per_page, 'offset': offset})
        # Memuat data twit ke dalam format yang sesuai
        twits_list = [{
            'id': twit.id,
            'username': twit.username,
            'twit_text': twit.twit_text,
            'date_post': twit.date_post.strftime('%Y-%m-%d %H:%M:%S'),
            'likes': twit.likes
        } for twit in twits]
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = url_for('user_followed', username=username, page=page + 1, _external=True)
        return jsonify({'twit_list': twits_list, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari twit pengguna', 'error': str(e)}), 500

if __name__ == '__main__':
	app.run()