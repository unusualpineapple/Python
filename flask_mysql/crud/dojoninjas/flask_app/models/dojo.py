from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('Dojos_Ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos


    @classmethod
    def save (cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"
        return connectToMySQL("Dojos_Ninjas").query_db(query, data)

    @classmethod
    def getoneandninjas (cls, data):
        query = "Select * from dojos left join ninjas on dojos.id = ninjas.dojos_id where dojos.id = %(id)s;"
        results = connectToMySQL('Dojos_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for nin in results:
            n = {
                'id':nin['ninjas.id'],
                'first_name':nin['first_name'],
                'last_name':nin['last_name'],
                'age':nin['age'],
                'created_at':nin['ninjas.created_at'],
                'updated_at':nin['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo


