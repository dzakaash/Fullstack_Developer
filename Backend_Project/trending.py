from flask import jsonify, request, url_for
from twiter import app, db
from twiter import Users, Twit
from sqlalchemy import text

# 19. Most popular user, utama
@app.route('/users/popular', methods=['GET'])
def popular_users():
    try:
        query = text("""
            SELECT u.username, u.first_name, u.last_name, COUNT(f.follower_id) AS followers_count
            FROM users u
            LEFT JOIN user_follows f ON u.id = f.followed_id
            GROUP BY u.username, u.first_name, u.last_name
            ORDER BY followers_count DESC
            LIMIT :limit
            OFFSET :offset
        """)
        data = request.get_json()
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        popular_users = db.session.execute(query, {'limit': per_page, 'offset': offset}).fetchall()
        users_list = []
        for user in popular_users:
            user_data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'followers_count': user.followers_count
            }
            users_list.append(user_data)
        total_users_count = db.session.execute(text("SELECT COUNT(*) FROM users")).scalar()
        total_pages = (total_users_count + per_page - 1) // per_page
        next_page = None
        if page < total_pages:
            next_page = url_for('popular_users', page=page + 1, _external=True)
        return jsonify({'popular_users': users_list, 'total_pages': total_pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengguna populer', 'error': str(e)}), 500

# 20. Most popular Twit, utama
@app.route('/twit/popular', methods=['GET'])
def popular_twits():
    try:
        query = text("""
            SELECT t.id, t.twit_text, t.user_id, t.date_post, COALESCE(COUNT(l.user_id), 0) AS likes
            FROM twit t
            LEFT JOIN "like" l ON t.id = l.twit_id
            GROUP BY t.id
            ORDER BY likes DESC
            LIMIT :limit
            OFFSET :offset
        """)
        # Mendapatkan parameter paginasi
        data = request.get_json()
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        # Eksekusi query untuk mendapatkan pengguna paling populer dengan parameter paginasi
        popular_twits = db.session.execute(query, {'limit': per_page, 'offset': offset}).fetchall()
        # Membuat daftar hasil pencarian twit paling populer
        twits_list = []
        for twit in popular_twits:
            twit_data = {
                'id': twit.id,
                'twit_text': twit.twit_text,
                'user_id': twit.user_id,
                'date_post': twit.date_post.strftime('%Y-%m-%d'),
                'likes_count': twit.likes
            }
            twits_list.append(twit_data)
        # Menghitung total halaman
        total_twits_count = db.session.execute(text("SELECT COUNT(*) FROM twit")).scalar()
        total_pages = (total_twits_count + per_page - 1) // per_page
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if page < total_pages:
            next_page = url_for('popular_twits', page=page + 1, _external=True)
        return jsonify({'popular_twits': twits_list, 'total_pages': total_pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari twit populer', 'error': str(e)}), 500

if __name__ == '__main__':
	app.run()