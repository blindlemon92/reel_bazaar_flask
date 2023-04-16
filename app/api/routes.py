from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, EntertainmentUnits, entertainment_units_schema, entertainment_units_schemas, rb_User, rb_user_schema, rb_users_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/entertainment-units', methods=['POST'])
@token_required
def create_entertainment_unit(current_user_token):
    unit_name = request.json['unit_name']
    unit_format = request.json['unit_format']
    unit_year = request.json['unit_year']
    unit_description = request.json['unit_description']
    unit_genre = request.json['unit_genre']
    unit_tone = request.json['unit_tone']
    unit_rating = request.json['unit_rating']
    key_actors = request.json['key_actors']
    user_token = current_user_token.token

    print(f'BIG TEST: {current_user_token.token}')

    entertainment_unit = EntertainmentUnits(unit_name, unit_format, unit_year, unit_description, unit_genre, unit_tone, unit_rating, key_actors, user_token = user_token )

    db.session.add(entertainment_unit)
    db.session.commit()

    response = entertainment_units_schema.dump(entertainment_unit)
    return jsonify(response)

@api.route('/entertainment-units', methods=['GET'])
@token_required
def get_entertainment_units(current_user_token):
    a_user = current_user_token.token
    entertainment_units = EntertainmentUnits.query.filter_by(user_token=a_user).all()
    response = entertainment_units_schemas.dump(entertainment_units)
    return jsonify(response)

@api.route('/entertainment-units/<id>', methods=['GET'])
@token_required
def get_entertainment_unit(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        entertainment_unit = EntertainmentUnits.query.get(id)
        response = entertainment_units_schema.dump(entertainment_unit)
        return jsonify(response)
    else:
        return jsonify({'message': 'Not Authorized'}), 401
    
@api.route('/entertainment-units/<id>', methods=['POST', 'PUT'])
@token_required
def update_entertainment_unit(current_user_token, id):
    entertainment_unit = EntertainmentUnits.query.get(id)
    entertainment_unit.unit_name = request.json['unit_name']
    entertainment_unit.unit_format = request.json['unit_format']
    entertainment_unit.unit_year = request.json['unit_year']
    entertainment_unit.unit_description = request.json['unit_description']
    entertainment_unit.unit_genre = request.json['unit_genre']
    entertainment_unit.unit_tone = request.json['unit_tone']
    entertainment_unit.unit_rating = request.json['unit_rating']
    entertainment_unit.key_actors = request.json['key_actors']
    entertainment_unit.user_token = current_user_token.token

    db.session.commit()
    response = entertainment_units_schema.dump(entertainment_unit)
    return jsonify(response)

@api.route('/entertainment-units/<id>', methods=['DELETE'])
@token_required
def delete_entertainment_unit(current_user_token, id):
    entertainment_unit = EntertainmentUnits.query.get(id)
    db.session.delete(entertainment_unit)
    db.session.commit()

    response = entertainment_units_schema.dump(entertainment_unit)
    return jsonify(response)

@api.route('/rb_users', methods=['POST'])
@token_required
def create_rb_user(current_user_token):
    user_name = request.json['user_name']
    user_genre = request.json['user_genre']
    user_format = request.json['user_format']
    user_favs = request.json['user_favs']
    user_token = current_user_token.token

    print(f'BIG TEST: {current_user_token.token}')

    rb_user = rb_User(user_name, user_genre, user_format, user_favs, user_token = user_token )

    db.session.add(rb_user)
    db.session.commit()

    response = rb_user_schema.dump(rb_user)
    return jsonify(response)

@api.route('/rb_users', methods=['GET'])
@token_required
def get_rb_users(current_user_token):
    a_user = current_user_token.token
    rb_users = rb_User.query.filter_by(user_token=a_user).all()
    response = rb_users_schema.dump(rb_users)
    return jsonify(response)

@api.route('/rb_users/<id>', methods=['GET'])
@token_required
def get_rb_user(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        rb_user = rb_User.query.get(id)
        response = rb_user_schema.dump(rb_user)
        return jsonify(response)
    else:
        return jsonify({'message': 'Not Authorized'}), 401
    
@api.route('/rb_users/<id>', methods=['POST'])
@token_required
def update_rb_user(current_user_token, id):
    rb_user = rb_User.query.get(id)
    rb_user.user_name = request.json['user_name']
    rb_user.user_genre = request.json['user_genre']
    rb_user.user_format = request.json['user_format']
    rb_user.user_favs = request.json['user_favs']
    rb_user.user_token = current_user_token.token

    db.session.commit()
    response = rb_user_schema.dump(rb_user)
    return jsonify(response)
    
@api.route('/rb_users/<id>', methods=['DELETE'])
@token_required
def delete_rb_user(current_user_token, id):
    rb_user = rb_User.query.get(id)
    db.session.delete(rb_user)
    db.session.commit()

    response = rb_user_schema.dump(rb_user)
    return jsonify(response)




