from twiter import app, db
from twiter import Users
from flask import request, jsonify, session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# 1. Register New Account, utama
@app.route('/register', methods=['POST'])
def register():
#json 'username', 'first_name', 'last_name', 'email, 'password', 'confirm_password', 'birth_date'
    data = request.get_json()
    # Mendapatkan data dari request
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    birth_date = data.get('birth_date')
    # Verifikasi bahwa password dan konfirmasi password sama
    if password != confirm_password:
        return jsonify({'message': 'Password dan konfirmasi password tidak cocok'}), 400
    # Hash password sebelum disimpan ke database
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    # Membuat author baru
    try:
      new_user = Users(
          username=username,
          first_name=first_name,
          last_name=last_name,
          email=email,
          password=hashed_password,
          birth_date=birth_date,
          last_activate=datetime.now().date(),
          last_activity='registrasi'
      )
      # Menyimpan author ke database
      db.session.add(new_user)
      db.session.commit()
      return jsonify({'message': 'Pendaftaran berhasil, Silahkan Login'}), 201
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat melakukan registrasi', 'error': str(e)}), 500

#2. Login
@app.route('/login', methods=['POST'])
def login():
    try:
      if 'user_id' in session:
            return jsonify({'message': 'Anda sudah login, silakan logout terlebih dahulu'}), 401
      auth = request.authorization
      user = Users.query.filter_by(username=auth.username).first()
      if user and check_password_hash(user.password, auth.password):
          session['user_id'] = user.id
          user.last_activate = datetime.now().date()
          user.last_activity = 'login'
          db.session.commit()
          return jsonify({'message': 'Login berhasil!'})
      else:
          return jsonify({'message': 'Username atau password salah!'}, 401)
    except Exception as e:
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
    
#3. Logout
@app.route('/logout', methods=['DELETE'])
def logout():
    try:
      if 'user_id' not in session:
        return {
        'message': 'Kamu belum log-in, silahkan melakukan login'
        }
      user_id = session['user_id']
      user = Users.query.get(user_id)
      user.last_activate = datetime.now().date()
      user.last_activity = 'logout'
      db.session.commit()
      session.pop('user_id', None)
      return jsonify({'message': 'Logout berhasil!'})
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500
  
# 4. Update User data, utama
@app.route('/profup', methods=['PUT'])
def profile_update():
#json 'username', 'first_name', 'last_name', 'email, 'password', 'birth_date'
    try:
      if 'user_id' not in session:
            return {
            'message': 'Kamu belum login, silahkan melakukan login'
        }
      user_id = session['user_id']
      user = Users.query.get(user_id)
      # Mendapatkan data dari request
      data = request.get_json()
      username = data.get('username')
      first_name = data.get('first_name')
      last_name = data.get('last_name')
      email = data.get('email')
      password = data.get('password')
      confirm_password = data.get('confirm_password')
      birth_date = data.get('birth_date')
      # Verifikasi bahwa password dan konfirmasi password sama
      if password != confirm_password:
          return jsonify({'message': 'Password dan konfirmasi password tidak cocok'}), 400
      if username :
        user.username = username
      if first_name :
        user.first_name = first_name
      if last_name :
        user.last_name = last_name
      if email :
        user.email = email
      if birth_date :
        user.birth_date = birth_date
      if password :
        # Hash password sebelum disimpan ke database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user.password = hashed_password
      # Menyimpan author ke database
      user.last_activate = datetime.now().date()
      user.last_activity = 'update-profile'
      db.session.commit()
      return jsonify({'message': 'Update profile berhasil!'}), 201
    except Exception as e:
      db.session.rollback()
      return jsonify({'message': 'Terjadi kesalahan saat menambahkan transaksi', 'error': str(e)}), 500

if __name__ == '__main__':
	app.run()