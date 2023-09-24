from flask import Blueprint, jsonify, abort, request
from src.models import User, db, Post, likes_table

bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    posts = Post.query.all()  # ORM performs SELECT query
    result = []
    for p in posts:
        result.append(p.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Post.query.get_or_404(id, "Post not found")
    return jsonify(p.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'user_id' not in request.json or 'message' not in request.json:
        return "No username or message"

    # user with id of user_id must exist
    User.query.get_or_404(request.json['user_id'], 'User not found')

    # construct Post
    p = Post(
        user_id=request.json['user_id'],
        message=request.json['message'],
    )

    db.session.add(p)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(p.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Post.query.get_or_404(id, "Post not found")
    try:
        db.session.delete(p)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):

    p = Post.query.get_or_404(id)

    p.message = request.json['message']

    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>/liking_users', methods=['GET'])
def liking_users(id: int):
    p = Post.query.get_or_404(id)
    result = []
    for u in p.liking_users:
        result.append(u.serialize())
    return jsonify(result)


