from flask_app.config.pymysqlconnection import MySQLConnection, connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
import re
from flask_app import app

EREG = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWupnum = re.compile(r'^[A-Z]+[0-9]')

bcrypt = Bcrypt(app)

class User:
    def __init__(self,data):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def grabuser(cls):
        query = 'select firstname, lastname from account'
        result = connectToMySQL('privatewall').query_db(query)
        return result

    @classmethod
    def insertuser(cls, data):
        query = 'insert into account (firstname, lastname, email, password, created_at, updated_at) values (%(firstname)s, %(lastname)s, %(email)s, %(password)s, NOW(), NOW());'
        result = connectToMySQL('privatewall').query_db(query,data)
        
        return result
    
    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * from account where email = %(email)s'
        result = connectToMySQL('privatewall').query_db(query,data)
        if len(result) <1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = 'select * from account where id = %(id)s'
        result = connectToMySQL('privatewall').query_db(query, data)
        return cls(result[0])

    @staticmethod
    def validation(result):
        is_valid = True
        query = 'select * from account where email = %(email)s'
        results = connectToMySQL('privatewall').query_db(query, result)
        if len(result['firstname']) <= 1:
            flash('dude how short is your name??')
            is_valid = False
        if len(result['lastname']) <= 1:
            flash('what country are you from????')
            is_valid = False
        if len(result['email']) <= 2:            
            flash('ha your email is too short try again')
            is_valid = False
        if len(results) >= 1:
            flash('wow buddy thats ther same one try again')
            is_valid = False
        # if not PWupnum.match(result['password']):
        #     flash('need to add an upper case and a number')
        #     is_valid = False
        if not EREG.match(result['email']):
            flash('hey dog your email isnt an email what you doing????????')
            is_valid = False
        if len(result['password']) <= 2:
            flash('your password is long make it longer')
            is_valid = False
        if not result['password'] == result['confirmpassword']:
            flash('you didnt have the same password fool')
            is_valid = False
        return is_valid
        

