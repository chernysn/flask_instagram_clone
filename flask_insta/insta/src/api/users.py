from flask import Blueprint, jsonify, abort, request
from src.models import User, db, Post, likes_table, friends_table
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    list_of_users = []
    for u in users:
        # build list of Tweets as dictionaries
        list_of_users.append(u.serialize())
    return jsonify(list_of_users)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id, "User not found")
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
 # req body must contain user_id and content
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)

    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)

    # construct User
    u = User(
        username=request.json['username'],
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        bio=request.json['bio'],
        password=scramble(request.json['password']),
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id, "User not found")
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):

    u = User.query.get_or_404(id)

    u.first_name = request.json['first_name']
    u.last_name = request.json['last_name']
    u.bio = request.json['bio']

    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>/liking_posts', methods=['GET'])
def liking_posts(id: int):
    u = User.query.get_or_404(id)
    result = []
    for t in u.liking_posts:
        result.append(t.serialize())
    return jsonify(result)


@bp.route('/<int:id>/friends/<int:fr_pk>/add', methods=['POST'])
def add_friends(id: int, fr_pk: int):

    u = User.query.get_or_404(id)
    f = User.query.get_or_404(fr_pk)

    u.friends_rel.append(f)
    db.session.commit()
    return f"Friend {f.username} was successfully added to User {u.username}."


@bp.route('/<int:id>/friends/<int:fr_pk>/delete', methods=['DELETE'])
def delete_friends(id: int, fr_pk: int):

    u = User.query.get_or_404(id)
    f = User.query.get_or_404(fr_pk)

    u.friends_rel.remove(f)
    db.session.commit()
    return f"Friend {f.username} was successfully deleted from User {u.username}."


@bp.route('/<int:id>/friends', methods=['GET'])
def friends(id: int):
    u = User.query.get_or_404(id)
    all_friends = []
    for f in u.friends_rel:
        friend = (f.id, f.username)
        all_friends.append(friend)
    return jsonify(all_friends)


@bp.route('/<int:id>/user_posts', methods=['GET'])
def user_posts(id):

    posts = Post.query.all()

    u = User.query.get_or_404(id)

    user_posts = []

    for post in posts:
        if post.user_id == u.id:
            a_post = f"{post.author.first_name.upper()} {post.author.last_name.upper()} posted a message: {post.message.upper()}"
            user_posts.append(a_post)

    return jsonify(user_posts)


@bp.route('/<int:id>/friends/<int:fr_pk>/posts', methods=['GET'])
def see_friends_posts(id, fr_pk):

    posts = Post.query.all()
    f = User.query.get_or_404(fr_pk)

    friend_posts = []

    for post in posts:
        if post.user_id == f.id:
            a_post = f"{post.author.first_name.upper()} {post.author.last_name.upper()} posted a message: {post.message.upper()}."
            friend_posts.append(a_post)

    return jsonify(friend_posts)
