from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    username = db.Column(db.String(80), unique=True) 
    password = db.Column(db.String(100)) 
    email = db.Column(db.String(100)) 
    
    goals = db.relationship("Goal", backref = "User")
    def __init__(self, username, password, email): 
        self.username = username 
        self.password = password 
        self.email = email 

class Group(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    name = db.Column(db.String(100)) 
    
    users = db.relationship("User", backref="Group")
    project = db.relationship("Project", backref="Group")
        
    def __init__(self, name):
        self.name = name 
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    title = db.Column(db.String(100), unique = True)
    dateStart = db.Column(db.DateTime)
    dateEnd = db.Column(db.DateTime) 
    
    goals = db.relationship("Goal", backref = "Project")
    def __init__(self, title, dateStart, dateEnd):
        self.title = title
        self.dateStart = dateStart
        self.dateEnd = dateEnd

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    goalName = db.Column(db.String(100), unique = True)
    isComplete = db.Column(db.Boolean) 
    dateComplete = db.Column(db.DateTime)  
