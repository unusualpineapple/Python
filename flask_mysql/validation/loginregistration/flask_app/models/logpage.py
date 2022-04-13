from flask_app.config.pymysqlconnection import MySQLConnection, connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
import re
from flask_app import app

EREG = re.compile(r'^{a-z-Z0-9.+_-] +@ [a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = app(Bcrypt)

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
        result = connectToMySQL('loginreg').query_db(query)
        return result

    @classmethod
    def insertuser(cls):
        query = 'insert into account (firstname, lastname, email, password, created_at, updated_at) values (%(firstname)s, %(lastname)s, %(email)s, %(password)s, NOW(), NOW()'
        result = connectToMySQL('loginreg').query_db(query)
        return result