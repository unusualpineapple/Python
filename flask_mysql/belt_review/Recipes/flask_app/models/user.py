from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

ereg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-Z]+$')


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
    def createuser(cls, data):
        query = 'insert into user (firstName, lastName, email, password, createdAt, updatedAt) values (%(firstName)s, %(lastName)s, %(email)s, %(password)s, NOW(), NOW());'
        result = connectToMySQL('recipes').query_db(query,data)
        return result
    
    @classmethod
    def getEmail(cls,data):
        query = 'select * from user where email = %(email)s'
        result = connectToMySQL('recipes').query_db(query,data)
        if len(result) <1:
            return False
        return cls(result[0])

    @classmethod
    def getByID(cls,data):
        query = 'select * from user where id = %(id)s'
        result = connectToMySQL('recipes').query_db(query,data)
        return cls(result[0])
    
    @staticmethod
    def validation(result):
        is_valid = True
        query = 'select * from user where email = %(email)s'
        results = connectToMySQL('recipes').query_db(query, result)
        if len(result['firstName']) <= 1:
            flash('your first name is blank?? try me')
            is_valid = False
        if len(result['lastName']) <= 1:
            flash('last name has no letters thats interesting')
            is_valid = False
        if len(result['email']) <= 5:            
            flash('is that really an email??')
            is_valid = False
        if len(results) >= 1:
            flash('already got that email goodbye')
            is_valid = False
        if not ereg.match(result['email']):
            flash('thats not an email try again')
            is_valid = False
        if len(result['password']) <= 5:
            flash('password too short')
            is_valid = False
        if not result['password'] == result['confirmpassword']:
            flash('you didnt have the same password')
            is_valid = False
        return is_valid