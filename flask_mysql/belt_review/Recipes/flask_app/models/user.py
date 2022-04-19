from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
from flask import flash
import re
from flask_app import app

ereg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)

class User:
    def __init__(self,data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def createuser(cls):
        query = 'insert into user (firstName, lastName, email, password) values (%(firstName)s, %(lastName)s, %(email)s, %(passwords)s)'
        result = connectToMySQL('recipes').query_db(query)
        return result
    
    @classmethod
    def getEmail(cls,data):
        query = 'select * from account where email = %(email)s'
        result = connectToMySQL('recipes').query_db(query,data)
        if len(result) <1:
            return False
        return cls(result[0])
    
    @staticmethod
    def validation(result):
        is_valid = True
        query = 'select * from account where email = %(email)s'
        results = connectToMySQL('recipes').query_db(query, result)
        if len(result['firstname']) <= 1:
            flash('dude how short is your name??')
            is_valid = False
        if len(result['lastname']) <= 1:
            flash('what country are you from????')
            is_valid = False
        if len(result['email']) <= 5:            
            flash('ha your email is too short try again')
            is_valid = False
        if len(results) >= 1:
            flash('wow buddy thats ther same one try again')
            is_valid = False
        if not EREG.match(result['email']):
            flash('hey dog your email isnt an email what you doing????????')
            is_valid = False
        if len(result['password']) <= 5:
            flash('your password is long make it longer')
            is_valid = False
        if not result['password'] == result['confirmpassword']:
            flash('you didnt have the same password fool')
            is_valid = False
        return is_valid