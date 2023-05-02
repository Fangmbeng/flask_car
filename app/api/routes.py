from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, Post, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'BMW': 'BMW-X3'}

@api.route('/posts', methods = ['POST'])
@token_required
def create_post(current_user_token):
    brand = request.json['brand']
    model = request.json['model']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    post = Post(brand, model, user_token = user_token )

    db.session.add(post)
    db.session.commit()

    response = contact_schema.dump(post)
    return jsonify(response)

@api.route('/posts', methods = ['GET'])
@token_required
def get_post(current_user_token):
    a_user = current_user_token.token
    post = Post.query.filter_by(user_token = a_user).all()
    response = contacts_schema.dump(post)
    return jsonify(response)

@api.route('/posts/<id>', methods = ['GET'])
@token_required
def get_post_two(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        post = Post.query.get(id)
        response = contact_schema.dump(post)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401

# UPDATE endpoint
@api.route('/contacts/<id>', methods = ['POST','PUT'])
@token_required
def update_postt(current_user_token,id):
    post = Post.query.get(id) 
    post.brand = request.json['brand']
    post.model = request.json['model']
    post.user_token = current_user_token.token

    db.session.commit()
    response = contact_schema.dump(post)
    return jsonify(response)


# DELETE car ENDPOINT
@api.route('/contacts/<id>', methods = ['DELETE'])
@token_required
def delete_contact(current_user_token, id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    response = contact_schema.dump(post)
    return jsonify(response)
