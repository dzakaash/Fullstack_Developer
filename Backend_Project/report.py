from flask import jsonify, request, url_for
from twiter import app, db
from twiter import Users
from datetime import datetime
from sqlalchemy import text

# 22. Incative User, utama
@app.route('/inactive')
def inactive_users():
    try:
        # Buat query untuk mendapatkan pengguna yang paling lama tidak aktif dan aktivitas terakhirnya
        query = text("""
            SELECT u.id, u.username, u.last_activate, u.last_activity
            FROM users u
            WHERE u.last_activate IS NOT NULL
            ORDER BY u.last_activate ASC
            LIMIT :limit OFFSET :offset
        """)
        # Mendapatkan parameter paginasi
        data = request.get_json()
        page = data.get('page', 1)
        per_page = 10
        offset = (page - 1) * per_page
        # Eksekusi query untuk mendapatkan pengguna paling populer dengan parameter paginasi
        inactive_users = db.session.execute(query, {'limit': per_page, 'offset': offset}).fetchall()
        # Membuat daftar hasil pencarian pengguna yang paling lama tidak aktif beserta aktivitas terakhirnya
        users_list = []
        for user in inactive_users:
            user_data = {
                'id': user.id,
                'username': user.username,
                'last_activate': user.last_activate.strftime('%Y-%m-%d') if user.last_activate else None,
                'last_activity': user.last_activity
            }
            users_list.append(user_data)
        # Menghitung total halaman
        total_users_count = db.session.execute(text("SELECT COUNT(*) FROM users WHERE last_activate IS NOT NULL")).scalar()
        total_pages = (total_users_count + per_page - 1) // per_page
        # Membuat URL untuk halaman selanjutnya jika ada
        next_page = None
        if page < total_pages:
            next_page = url_for('inactive_users', page=page + 1, _external=True)
        return jsonify({'inactive_users': users_list, 'total_pages': total_pages, 'next_page': next_page}), 200
    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan saat memuat daftar pengguna tidak aktif', 'error': str(e)}), 500

if __name__ == '__main__':
	app.run()