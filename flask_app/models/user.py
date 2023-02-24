from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}" #simple function to get full name

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users ORDER BY first_name;"

        results = connectToMySQL(cls.db).query_db(query)

        user = []
        for x in results:
            user.append(cls(x))
        return user
    
    @classmethod
    def get_one(cls, id):
        query = """
            SELECT * FROM users
            WHERE id = %(id)s;
        """
        data = {
            'id':id
            }
        
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])


    @classmethod
    def save_user(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        #This will return the new row ID
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def update(cls, data):
        query = """
            UPDATE users
            SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s
            WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def delete(cls, id):

        query = """
            DELETE FROM users
            WHERE id=%(id)s;
        """
        data = {
            'id':id
        }

        return connectToMySQL(cls.db).query_db(query, data)
        