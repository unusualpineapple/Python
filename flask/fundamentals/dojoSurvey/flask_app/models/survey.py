from flask_app.config.pymysqlconnection import MySQLConnection, connectToMySQL
from flask import flash

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.codinglanguage = ['codinglanguage']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def graball(cls):
        query = 'select * from dojostable;'
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        people = []
        for p in results:
            people.append (cls(p))
        return people

    @classmethod
    def save (cls,data):
        query = "insert into dojostable (name,location,language,comment, codinglanguage, created_at, updated_at) values (%(name)s, %(location)s, %(language)s, %(comment)s, %(codinglanguage)s,NOW(), NOW());"
        return connectToMySQL('dojo_survey_schema'). query_db(query,data)
    
    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 character.")
            is_valid = False
        if len(survey['location']) < 3:
            flash("Hey buddy need at least 3 characters.")
            is_valid = False
        if len(survey['language']) < 3:
            flash("What you dont speak PICK ONE")
            is_valid = False
        if len(survey['codinglanguage']) < 3:
            flash("Why did you not pick SOMETHING TO LEARN PICK ONE")
            is_valid = False
        return is_valid

    @classmethod
    def getone(cls):
        query = "select * from dojostable order by dojostable.id desc limit 1; "
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Survey(results[0])