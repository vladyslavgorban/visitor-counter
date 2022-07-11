import os

SECRET_KEY = os.getenv('SECRET_KEY')
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DATABASE_NAME = os.environ['DATABASE_NAME']
# DB_URI = 'mysql://bb3402207d45c8:f7d3753e@us-cdbr-east-05.cleardb.net/heroku_f06bf28282c42fd?reconnect=true'
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI