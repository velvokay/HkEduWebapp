from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy 
from models import * 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye Friends"

@app.route("/square/<value>")
def return_square(value):
    result = square(int(value))
    return result 

def square(x): 
    result = x * x
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
