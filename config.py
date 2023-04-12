from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_METHODS'] = 'POST'
# app.config['CORS_ORIGINS'] = ['http://localhost:5000']
# app.config['CORS_SUPPORTS_CREDENTIALS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-book-app-database.db'
