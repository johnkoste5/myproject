from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_courses(self):
        query = "SELECT * from courses"
        return self.db.query_db(query)

    def add_course(self, baboon):
        print "in the model, line 12", baboon
        query = "INSERT INTO courses (name, description, created_at) VALUES (:name, :description, NOW())"
        monkey = {
            'name': baboon['name'],
            'description': baboon['description']
        }
        return self.db.query_db(query, monkey)

    def get_course(self, id):
        query = "SELECT * FROM courses WHERE id=:id"
        values = {
            'id': id
        }
        return self.db.query_db(query, values)

    def destroy(self, id):
        query = "DELETE FROM courses WHERE id=:id"
        values = {
            'id': id
        }
        self.db.query_db(query, values)