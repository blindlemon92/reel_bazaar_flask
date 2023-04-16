import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
        set config variables for app
        with environment variables if set
        else create them
    '''

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY') or 'XENOMORPH'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False

