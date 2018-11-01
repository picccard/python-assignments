from flask import Flask

app = Flask(__name__)
# import secrets -> secrets.token_hex(16)
app.config['SECRET_KEY'] = '0b23102c6ef9982b232a0423349365f0'

from multimedia import routes
