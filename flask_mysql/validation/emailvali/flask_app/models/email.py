from flask_app.config.pymysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^{a-z-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def grabemails(cls):
        query = 'select * from email'
        result = connectToMySQL('emails').query_db(query)
        emails = []
        for e in result:
            emails.append (cls(e))
        return emails

    @classmethod
    def submitemail(cls, data):
        query = 'insert into email (email, created_at, updated_at) values (%(email)s, NOW(), NOW())'
        return connectToMySQL('emails').query_db(query, data)
    
    @classmethod
    def deleteemail(cls, data):
        query = 'delete from email where id = %(id)s'
        return connectToMySQL('emails').query_db(query,data)
    
    
    @staticmethod
    def validate(email):
        is_valid = True 
        if len(email['email']) <= 1:
            flash('thats not good try again')
            is_valid = False 
        elif EMAIL_REGEX.match(email['email']):
            flash('YO UR EMAIL IS THE SAME MAKE A NEW ONE')
            is_valid = False
        else:
            flash ('look at you you made a good one ' + email['email'] + ' so proud thankssssss')
            is_valid = True
        return is_valid
