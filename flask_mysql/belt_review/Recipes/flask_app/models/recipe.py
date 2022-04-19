from unittest import result
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
        query = 'insert into creations (name, description, instructions, date, time, user_id) values (%(name)s, %(description)s, %(instructions)s, %(date)s, %(time)s, %(user_id)s);'
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def getCreations(cls):
        query = 'select * from creations;'
        result = connectToMySQL(cls.db).query_db(query)
        allCreations=[]
        for creation in result:
            print(creation['date'])
            allCreations.append(cls(creation))
        return allCreations

    @classmethod
    def getOneCreation(cls,data):
        query = 'select * from creations where id=%(id)s'
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def updateCreation(cls,data):
        query='update creations set name=%(name)s, description=%(description)s, instructions=%(instructions)s, date=%(date)s, time=%(time)s, updatedAt=NOW() where id=%(id)s'
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def deleteCreation(cls,data):
        query ='delete from creations where id=%(id)s'
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @staticmethod
    def validate(creation):
        is_valid = True
        if len(creation['name']) <= 3:
            flash('is that really a name??')
            is_valid = False
        if len(creation['description']) <10:
            flash('well that TOLD ME NOTHING')
            is_valid = False
        if len(creation['instructions']) <10:
            flash('how DO I MAKE ITTTTT')
            is_valid = False
        if creation['date'] == "":
            flash('enter a date')
            is_valid = False
        return is_valid


