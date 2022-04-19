from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Creation:
    db = 'recipes'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.time = data['time']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
    
    @classmethod
    def save(cls,data):
        query = 'insert into creations (name, description, instruction, date, time, user_id) values (%(name)s, %(description)s, %(instructions)s, %(date)s, %(time)s, %(user_id)s);'
        result = connectToMySQL(cls.db).query_db(query,data)
        return result