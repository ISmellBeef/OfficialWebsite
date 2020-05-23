from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app.services import *

api.add_resource(UserLogin,"/api/user/login")
api.add_resource(UserRegister,"/api/user/register")
api.add_resource(UserDelete,"/api/user/delete")
api.add_resource(UserQuery,"/api/user/query")

from app.routes import *