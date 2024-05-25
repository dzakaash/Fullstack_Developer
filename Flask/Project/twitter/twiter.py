from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/twiter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)

user_follows = Table(
    'user_follows',
    db.metadata,
    db.Column('follower_id', db.Integer, ForeignKey('users.id'), primary_key=True),
    db.Column('followed_id', db.Integer, ForeignKey('users.id'), primary_key=True)
)
# db.metadata dalam SQLAlchemy digunakan untuk menyimpan metadata yang terkait dengan struktur tabel dalam basis data.

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    last_activate = db.Column(db.Date)
    last_activity = db.Column(db.String)
    # Relations
    twits = db.relationship('Twit', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')
    liked_twits = db.relationship('Like', back_populates='user')
    followers = db.relationship('Users',
                                secondary=user_follows,
                                primaryjoin=(id == user_follows.c.follower_id),
                                secondaryjoin=(id == user_follows.c.followed_id),
                                backref='following'
                                )

    def __repr__(self):
        return f'<User: {self.username}>'

class Twit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String, nullable=False)
    twit_text = db.Column(db.String(280), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    date_post = db.Column(db.DateTime)
    # Relations
    user = db.relationship('Users', back_populates='twits')
    comments = db.relationship('Comment', back_populates='twit')
    likes = db.relationship('Like', back_populates='twit')
    retweeted_by = db.relationship('Users',
                                   secondary='retweets',
                                   primaryjoin='Twit.id == retweets.c.retweeted_id',
                                   secondaryjoin='Twit.id == retweets.c.retweet_id',
                                   backref='retweeted_twits'
                                   )

    def __repr__(self):
        return f'<Twit: {self.twit_text}>'

retweets = db.Table('retweets',
                    db.Column('retweet_id', db.Integer, ForeignKey('twit.id'), primary_key=True),
                    db.Column('retweeted_id', db.Integer, ForeignKey('twit.id'), primary_key=True)
                    )

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String, nullable=False)
    comment_text = db.Column(db.String(280), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    twit_id = db.Column(db.Integer, ForeignKey("twit.id"), nullable=False)
    date_post = db.Column(db.DateTime)
    like = db.Column(db.Integer, default=0)
    # Relations
    twit = db.relationship('Twit', back_populates='comments')
    user = db.relationship('Users', back_populates='comments')

    def __repr__(self):
        return f'<Comment: {self.comment_text}>'

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    twit_id = db.Column(db.Integer, ForeignKey('twit.id'), nullable=False)
    # Relations
    user = db.relationship('Users', back_populates='liked_twits')
    twit = db.relationship('Twit', back_populates='likes')

with app.app_context():
    db.create_all()

from flask_migrate import Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()