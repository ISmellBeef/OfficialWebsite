from flask import Flask, redirect, jsonify,request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user
from flask_restful import Resource,Api, reqparse
import json

parser = reqparse.RequestParser()
parser.add_argument('username', type = str)
parser.add_argument('password', type = str)
parser.add_argument('email', type = str)
class UserLogin(Resource):
   def post(self):
      args = request.get_json()
      user = User.query.filter_by(email=args['email']).first()
      v = args['password']
      try:
         valid = bcrypt.check_password_hash(user.password, v)
      except:
         if v == user.password:
            valid = True
         else:
            valid = False
      if user and valid:
         return jsonify({'succeed':'true'})
      else:    
         return jsonify({'succeed':'false'})

class UserRegister(Resource):
   def put(self):
      args = request.get_json()
      hashed_password = bcrypt.generate_password_hash(args['password']).decode('utf-8')
      user = User(username=args['username'], email=args['email'], password=hashed_password)
      db.session.add(user)
      db.session.commit()
      return jsonify({'succeed':'true'})

class UserDelete(Resource):
   def delete(self):
      args = request.args
      user = User.query.filter_by(email=args["email"]).first()
      db.session.delete(user)
      db.session.commit()
      return jsonify({'succeed':'true'})

class UserQuery(Resource):
   def get(self):
      args = request.args
      users = User.query.filter(User.username.like(args["username"])).all()
      users_dict = []
      for u in users:
        user_dict = {
           'username': u.username,
           'email': u.email
        }
        users_dict.append(user_dict)
      return jsonify({'users':users_dict})