from twiter import app, db
from twiter import Users, Twit, Comment, Like
from flask import request, jsonify, session
from datetime import datetime
import uuid
from sqlalchemy import text

twit = None

# 5. Post a Tweet, utama
@app.route('/twit/create', methods=['POST'])
def create_twit():
    try:
        #json 'twit_text'
        if 'user_id' not in session:
            return {
            'message': 'Kamu belum log-in, silahkan melakukan login'
        }
        user_id = session['user_id']
        user = Users.query.get(user_id)
        # Mendapatkan data twit dari request
        data = request.get_json()
        twit_text = data.get('twit_text')
        # Membuat ID publik untuk kutipan baru
        public_id = str(uuid.uuid4())
        # Mendapatkan tanggal saat ini
        date_post = datetime.now().date()
        # Membuat kutipan baru
        new_twit = Twit(
            public_id=public_id,
            twit_text=twit_text,
            user_id=user_id,
            date_post=date_post
        )
        # Menyimpan kutipan baru ke dalam database
        db.session.add(new_twit)
        # Update aktivitas pengguna
        user.last_activate = datetime.now().date()
        user.last_activity = 'membuat twit'
        db.session.commit()
        # Menyiapkan respons
        response_data = {
            'id': new_twit.public_id,
            'twit': new_twit.twit_text,
            'username': user.username,  # Mengambil username dari pengguna
            'date': new_twit.date_post.strftime('%Y-%m-%d')
            }
        return jsonify(response_data), 201
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat membuat twit', 'error': str(e)}), 500
    
# 6. Post a Retweet
@app.route('/twit/retweet', methods=['POST'])
def create_retweet():
  # json 'twit_text', 'twit_id' = public_id
    try:
        # Periksa apakah pengguna telah masuk
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum login, silakan login terlebih dahulu'}), 401
        # Mendapatkan user_id dari session
        user_id = session['user_id']
        # Mendapatkan data twit dari request
        data = request.get_json()
        twit_text = data.get('twit_text')
        # mendapatkan id twit yang di retweet
        twit_id = data.get('twit_id')
        # Mendapatkan tanggal saat ini
        date_post = datetime.now().date()
        # Membuat ID publik untuk retweet baru
        public_id = str(uuid.uuid4())
        # Membuat retweet baru
        new_retweet = Twit(
            public_id=public_id,
            twit_text=twit_text,
            user_id=user_id,
            date_post=date_post
        )
        # Menyimpan retweet baru ke dalam database
        db.session.add(new_retweet)
        # Temukan twit yang akan diretweet
        twit_to_retweet = Twit.query.filter_by(public_id=twit_id).first()
        # Menambahkan retweet ke twit yang akan diretweet
        if twit_to_retweet:
            query = text("""
                INSERT INTO retweets (retweet_id, retweeted_id)
                VALUES (:twit_to_retweet_id, (SELECT id FROM twit WHERE public_id = :public_id))
            """)
            db.session.execute(query, {"twit_to_retweet_id": twit_to_retweet.id, "public_id": public_id})
        db.session.commit()
        # Update aktivitas pengguna
        user = Users.query.get(user_id)
        user.last_activate = datetime.now().date()
        user.last_activity = 'membuat retweet'
        db.session.commit()
        # Format data retweet ke dalam format JSON untuk ditampilkan sebagai respons
        retweet_data = {
            'id': public_id,
            'twit': twit_text,
            'username': user.username,
            'date': date_post.strftime('%Y-%m-%d'),
            'retweet': twit_id
        }
        return jsonify(retweet_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat membuat retweet', 'error': str(e)}), 500

# 7. Like a Tweet, utama
@app.route('/twit/like', methods=['POST'])
def like_twit():
    # json "twit_id" = public_id
    global twit  # Use the global variable 'twit'
    try:
        # Periksa apakah pengguna telah masuk
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum login, silakan login terlebih dahulu'}), 401
        # Temukan pengguna berdasarkan user_id dari session
        user_id = session['user_id']
        user = Users.query.get(user_id)
        # mendapatkan twit_id
        data = request.get_json()
        twit_id = data.get('twit_id')
        # Temukan twit berdasarkan public_id
        twit = Twit.query.filter_by(public_id=twit_id).first()
        if not twit:
            return jsonify({'message': 'Twit tidak ditemukan'}), 404
        # Periksa apakah pengguna sudah menyukai twit ini sebelumnya menggunakan raw query
        like_query = text("""
            SELECT * FROM "like" WHERE user_id = :user_id AND twit_id = :twit_id
        """)
        existing_like = db.session.execute(like_query, {'user_id': user_id, 'twit_id': twit.id}).fetchone()
        if existing_like:
            return jsonify({'message': 'Anda sudah menyukai twit ini!'}), 400
        # Insert like ke dalam tabel Like
        insert_query = text("""
            INSERT INTO "like" (user_id, twit_id) VALUES (:user_id, :twit_id)
        """)
        db.session.execute(insert_query, {'user_id': user_id, 'twit_id': twit.id})
        db.session.commit()
        # Update aktivitas pengguna
        user.last_activate = datetime.now().date()
        user.last_activity = f'menyukai twit dengan id {twit_id}'
        db.session.commit()
        # Format data twit ke dalam format JSON untuk ditampilkan sebagai respons
        twit_data = {
            'id': twit.public_id,
            'twit': twit.twit_text,
            'username': twit.user.username,
            'date': twit.date_post.strftime('%Y-%m-%d'),
            'likes': len(twit.likes),
        }
        return jsonify(twit_data), 200
    except Exception as e:
        db.session.rollback()
        # Check if 'twit' is assigned before accessing its 'id' attribute
        twit_id = getattr(twit, 'id', None)
        return jsonify({'message': 'Terjadi kesalahan saat menyukai twit', 'error': str(e), 'twit': twit_id}), 500
    
# 8. unlike a Tweet
@app.route('/twit/unlike', methods=['DELETE'])
def unlike_twit():
    # json "twit_id" = public_id
    try:
        # Periksa apakah pengguna telah login
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum login, silakan login terlebih dahulu'}), 401
        # Temukan pengguna berdasarkan user_id dari session
        user_id = session['user_id']
        user = Users.query.get(user_id)
        # mendapatkan twit_id
        data = request.get_json()
        twit_id = data.get('twit_id')
        # Temukan twit berdasarkan public_id
        twit = Twit.query.filter_by(public_id=twit_id).first()
        if not twit:
            return jsonify({'message': 'Twit tidak ditemukan'}), 404
        # Periksa apakah pengguna telah menyukai twit ini sebelumnya
        like = Like.query.filter_by(user_id=user.id, twit_id=twit.id).first()
        if not like:
            return jsonify({'message': 'Anda belum menyukai twit ini!'}), 400
        # Hapus like dari tabel Like
        db.session.delete(like)
        db.session.commit()
        # Update aktivitas pengguna
        user.last_activate = datetime.now().date()
        user.last_activity = f'berhenti menyukai twit dengan id {twit_id}'
        db.session.commit()
        return jsonify({'message': 'Anda membatalkan menyukai twit ini!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat membatalkan menyukai twit', 'error': str(e)}), 500
    
# 9. Comment Tweet
@app.route('/twit/comment', methods=['POST'])
def comment_twit():
    try:
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum login, silakan login terlebih dahulu'}), 401
        user_id = session['user_id']
        data = request.get_json()
        comment_text = data.get('comment_text')
        twit_id = data.get('twit_id')
        date_post = datetime.now().date()
        twit = Twit.query.filter_by(public_id=twit_id).first()
        if not twit:
            return jsonify({'message': 'Twit tidak ditemukan'}), 404
        # Buat public_id yang unik untuk komentar
        public_id = str(uuid.uuid4())
        new_comment = Comment(
            public_id=public_id,  # Tambahkan public_id yang unik
            comment_text=comment_text,
            user_id=user_id,
            twit_id=twit.id,
            date_post=date_post,
            like=0
        )
        db.session.add(new_comment)
        db.session.commit()
        user = Users.query.get(user_id)
        user.last_activate = datetime.now().date()
        user.last_activity = f'memberi komentar kepada twit dengan id {twit_id}'
        db.session.commit()
        comment_data = {
            'public_id': public_id,  # Sertakan public_id dalam respons
            'comment': new_comment.comment_text,
            'username': user.username,
            'date': date_post.strftime('%Y-%m-%d'),
            'twit_id': twit.id,
        }
        return jsonify(comment_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat menambahkan komentar', 'error': str(e)}), 500

# 10. Delete Comment
@app.route('/comment', methods=['DELETE'])
def delete_comment():
    # json 'comment_id'
    try:
        # Periksa apakah pengguna sudah login
        if 'user_id' not in session:
            return jsonify({'message': 'Anda belum login, silakan login terlebih dahulu'}), 401
        # Mendapatkan user_id dari session
        user_id = session['user_id']
        # Mendapatkan comment_id
        data = request.get_json()
        comment_id = data.get('comment_id')
        # Temukan komentar berdasarkan comment_id
        comment = Comment.query.filter_by(public_id=comment_id).first()
        if not comment:
            return jsonify({'message': 'Komentar tidak ditemukan'}), 404
        # Periksa apakah pengguna adalah pemilik komentar
        if comment.user_id != user_id:
            return jsonify({'message': 'Anda tidak memiliki izin untuk menghapus komentar ini'}), 403
        # Hapus komentar dari database
        db.session.delete(comment)
        db.session.commit()
        # Update aktivitas pengguna
        user = Users.query.get(user_id)
        user.last_activate = datetime.now().date()
        user.last_activity = f'mengghapus komentar dengan id {comment_id}'
        db.session.commit()
        return jsonify({'message': 'Komentar berhasil dihapus'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Terjadi kesalahan saat menghapus komentar', 'error': str(e)}), 500

if __name__ == '__main__':
	app.run()