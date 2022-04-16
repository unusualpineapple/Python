from flask_app.config.pymysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app

class Message:
    def __init__(self,data):
        self.id = data['id']
        self.sender_id = data['sender_id']
        self.sender_name = data['sender_name']
        self.receiver_id = data['receiver_id']
        self.receiver_name = data['receiver_name']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getallmessages():
        query = 'select * from messages'
        result = connectToMySQL('privatewall').query_db(query)
        return result
    
    @classmethod
    def savemessage():
        query = 'insert into messages (message, created_at, updated_at) values (%(messages)s, NOW(), NOW())'
        result = connectToMySQL('privatewall').query_db(query)
        return result
    
    @classmethod
    def getfromid():
        query = 'select * from accounts as sender join messages on sender.id = messages.sender_id join accounts as receiver on receiver.id = messages.receiver_id'
        result = connectToMySQL('privatewall').query_db(query)
        return result

    @classmethod
    def removemessage():
        query='delete from messages where sender_id = %(sender_is)s'
        result = connectToMySQL('privatewall').query_db(query)
        return result

    @staticmethod
    def validatemessage():
        is_valid = True
        query = 'select * from messages where message = %(message)s'
        result = connectToMySQL('privatewall').query_db(query)
        if len(result['message']) <= 1:
            flash('EH IF YOU AINT GOT NOTHING TO SAY DONT SAY NOTHIN')
            is_valid = False
        return is_valid
