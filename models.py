from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database' 
    
class EntertainmentUnits(db.Model):
    id = db.Column(db.String, primary_key=True)
    unit_name = db.Column(db.String(150), nullable=False)
    unit_format = db.Column(db.String(150), nullable=True)
    unit_year = db.Column(db.String(150), nullable=True)
    unit_description = db.Column(db.String(400), nullable=True)
    unit_genre = db.Column(db.String(150), nullable=True)
    unit_tone = db.Column(db.String(150), nullable=True)
    unit_rating = db.Column(db.String(150), nullable=True)
    key_actors = db.Column(db.String(150), nullable=True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, unit_name, unit_format, unit_year, unit_description, unit_genre, unit_tone, unit_rating, key_actors, user_token, id = '' ):
        self.id = self.set_id()
        self.unit_name = unit_name
        self.unit_format = unit_format
        self.unit_year = unit_year
        self.unit_description = unit_description
        self.unit_genre = unit_genre
        self.unit_tone = unit_tone
        self.unit_rating = unit_rating
        self.key_actors = key_actors
        self.user_token = user_token

    def __repr__(self):
        return f'{self.unit_name} has been put in the database'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class EntertainmentUnitsSchema(ma.Schema):
    class Meta:
        fields = ['id', 'unit_name', 'unit_format', 'unit_year', 'unit_description', 'unit_genre', 'unit_tone', 'unit_rating', 'key_actors']

entertainment_units_schema = EntertainmentUnitsSchema()
entertainment_units_schemas = EntertainmentUnitsSchema(many=True)

class rb_User(db.Model):
    id = db.Column(db.String, primary_key=True)
    user_name = db.Column(db.String(150), nullable=False)
    user_genre = db.Column(db.String(150), nullable=True)
    user_format = db.Column(db.String(150), nullable=True)
    user_favs = db.Column(db.String(150), nullable=True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)

    def __init__(self, user_name, user_genre, user_format, user_favs, user_token, id=''):
        self.id = self.set_id()
        self.user_name = user_name
        self.user_genre = user_genre
        self.user_format = user_format
        self.user_favs = user_favs
        self.user_token = user_token   

    def __repr__(self):
        return f'{self.user_name} has been put in the database'
    
    def set_id(self):
        return (secrets.token_urlsafe())

class rb_UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'user_name', 'user_genre', 'user_format', 'user_favs']

rb_user_schema = rb_UserSchema()
rb_users_schema = rb_UserSchema(many=True)



    
