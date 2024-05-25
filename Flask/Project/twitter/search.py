from twiter import app, db
from twiter import Users, Twit
from flask import request, jsonify, url_for
from sqlalchemy import text

# 17. Cari Pengguna, utama
@app.route('/users', methods=['GET'])
def users_by_keywords():
    try:
        # mendapatkan keywords, json 'keywords', 'page'
        data = request.get_json()
        keywords = data.get('keywords')
        if not keywords:
            return jsonify({'message': 'Kata kunci tidak ditemukan'}), 400
        # Mendapatkan parameter paginasi
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        # Query untuk mencari pengguna berdasarkan kata kunci dalam username, first_name, atau last_name
        query = text(f"""
            SELECT username, first_name, last_name 
            FROM users 
            WHERE username ILIKE '%%{keywords}%%' OR first_name ILIKE '%%{keywords}%%' OR last_name ILIKE '%%{keywords}%%'
            ORDER BY username
            LIMIT :limit
            OFFSET :offset
        """)
        # Eksekusi query untuk mendapatkan data pengguna dengan parameter paginasi
        users = db.session.execute(query, {'limit': per_page, 'offset': offset}).fetchall()
        # Membuat daftar pengguna dari hasil query
        users_list = [{
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        } for user in users]
        # Menghitung total halaman dan jumlah pengguna
        total_data = len(users_list)
        total_pages = (total_data + per_page - 1) // per_page
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if page < total_pages:
            next_page = url_for('users_by_keywords', keywords=keywords, page=page + 1, _external=True)
        # Mendapatkan daftar pengguna pada halaman tertentu
        start_index = (page - 1) * per_page
        end_index = min(start_index + per_page, total_data)
        users_list_page = users_list[start_index:end_index]
        return jsonify({'users': users_list_page, 'total_pages': total_pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari pengguna', 'error': str(e)}), 500

# 18. search Twit, utama
@app.route('/twit/', methods=['GET'])
def twits_by_keywords():
    try:
        # mendapatkan keywords, json 'keywords', 'page'
        data = request.get_json()
        keywords = data.get('keywords')
        if not keywords:
            return jsonify({'message': 'Kata kunci untuk pencarian twit tidak ditemukan'}), 400
        # Mendapatkan parameter paginasi
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        # Membuat query untuk mencari twit berdasarkan kata kunci dengan paginasi
        query = text(f"""
            SELECT t.public_id, t.twit_text, t.user_id, t.date_post,
                COALESCE(COUNT(l.user_id), 0) AS likes
            FROM twit t
            LEFT JOIN "like" l ON t.id = l.twit_id
            WHERE t.twit_text ILIKE '%%{keywords}%%'
            GROUP BY t.public_id, t.twit_text, t.user_id, t.date_post
            ORDER BY likes DESC
            LIMIT :limit
            OFFSET :offset
        """)
        # Eksekusi query untuk mendapatkan twit dengan parameter paginasi
        twits = db.session.execute(query, {'limit': per_page, 'offset': offset}).fetchall()
        # Membuat daftar hasil pencarian twit
        twits_list = []
        for twit in twits:
            twit_data = {
                'id': twit.public_id,
                'twit_text': twit.twit_text,
                'username': twit.user_id,
                'date': twit.date_post.strftime('%Y-%m-%d'),
                'likes': twit.likes,
            }
            twits_list.append(twit_data)
        # Menghitung total halaman
        total_pages = (len(twits) + per_page - 1) // per_page
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if page < total_pages:
            next_page = url_for('twits_by_keywords', keywords=keywords, page=page + 1, _external=True)
        return jsonify({'twits': twits_list, 'total_pages': total_pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat mencari twit', 'error': str(e)}), 500


if __name__ == '__main__':
	app.run()