from hello_rubbish import db


tags = db.Table('tags',
              db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
              db.Column('course_id', db.Integer, db.ForeignKey('course.id')))


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    course = db.relationship('Course', secondary=tags)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "name:%r" % self.name


class Course(db.Model):
    ___tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    # student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "name:%r" % self.name
