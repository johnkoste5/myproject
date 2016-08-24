from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        courses = self.models['Course'].get_courses()
        print "all courses", courses
        return self.load_view('index.html', courses=courses)

    def add_course(self):
        print "in the controller, line 15", request.form
        course_id = self.models['Course'].add_course(request.form)
        print "new course id", course_id
        return redirect('/')

    def confirm_delete(self, id):
        print id
        course = self.models['Course'].get_course(id)
        print course
        return self.load_view('delete.html', course=course[0])

    def destroy(self, id):
        print id
        self.models['Course'].destroy(id)
        return redirect('/')
