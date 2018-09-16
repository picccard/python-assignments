from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '0b23102c6ef9982b232a0423349365f0' # import secrets > secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# Makes sure site.db is created
# If it already exist, the old is used
from blog.models import Article
db.create_all()

from blog import routes
