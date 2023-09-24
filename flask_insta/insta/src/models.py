from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()  # database adapter object


friends_table = db.Table(
    'friends_table',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),

    db.Column(
        'friend_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), unique=False, nullable=True)
    last_name = db.Column(db.String(128), unique=False, nullable=True)
    bio = db.Column(db.String(500), unique=False, nullable=True)
    liking_posts = db.relationship('Post', backref='user', cascade="all,delete")
    posts = db.relationship("Post", backref="author")
    friends = db.relationship('User', secondary=friends_table,
        primaryjoin = (friends_table.c.friend_id == id),
        secondaryjoin = (friends_table.c.user_id == id),
        backref = db.backref('friends_rel', lazy = 'dynamic'), 
        lazy = 'dynamic')

    def __init__(self, username: str, password: str, first_name: str, last_name: str, bio: str):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'bio': self.bio,
        }

likes_table = db.Table(
    'likes',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),

    db.Column(
        'post_id', db.Integer,
        db.ForeignKey('posts.id'),
        primary_key=True
    ),

    db.Column(
        'created_at', db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    liking_users = db.relationship(
        'User', secondary=likes_table,
        lazy='subquery',
        backref=db.backref('liked_posts', lazy=True)
    )

    def __init__(self, message: str, user_id: int):
        self.message = message
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        }
