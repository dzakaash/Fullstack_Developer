from twiter import app, db
from twiter import Twit, Users
from flask import jsonify, request, url_for, session
from sqlalchemy import text

# 21. Home
@app.route('/')
def home():
    # json "page"
    try:
        # Periksa apakah pengguna sudah login
        if 'user_id' not in session:
            return {'message': 'Selamat datang di Twiter, silahkan login atau register'}
        else:
            user_id = session['user_id']
            # Buat query untuk mendapatkan twit terbaru dari pengguna yang diikuti oleh pengguna yang sedang login
            page = request.args.get('page', 1, type=int)
            per_page = 10
            offset = (page - 1) * per_page
            # Eksekusi query dengan parameter 'limit' dan 'offset'
            twits = db.session.execute(text("""
                SELECT t.id, t.twit_text, t.user_id, t.date_post
                FROM twit t
                WHERE t.user_id IN (
                    SELECT followed_id
                    FROM user_follows
                    WHERE follower_id = :user_id
                )
                ORDER BY t.date_post DESC
                LIMIT :limit OFFSET :offset
            """), {'user_id': user_id, 'limit': per_page, 'offset': offset}).fetchall()
            # Membuat daftar hasil pencarian twit terbaru dari pengguna yang diikuti
            twits_list = []
            for twit in twits:
                twit_data = {
                    'id': twit.id,
                    'twit_text': twit.twit_text,
                    'user_id': twit.user_id,
                    'date_post': twit.date_post.strftime('%Y-%m-%d')
                }
                twits_list.append(twit_data)
            # Membuat URL untuk halaman selanjutnya jika ada
            next_page = None
            next_page = url_for('home', page=page + 1, _external=True)
            return jsonify({'twits': twits_list, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat memuat halaman', 'error': str(e)}), 500

if __name__ == '__main__':
	app.run()