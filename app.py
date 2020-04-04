from flask import Flask , request , url_for , render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////artists.db'
db = SQLAlchemy(app)  

class Artist(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    genre = db.Column(db.String)
    

# creates the table
db.create_all()


@app.route('/')
def hello_world():
    return 'Helqlod, Worlqwdd!'

@app.route('/about')
def about():
    return 'About page'

@app.route('/user/<username>')
def profile(username):
    return '{}'.format(username)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html' , name=name)
    

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return about()
#     else:
#         return hello_world()    
if __name__ == "__main__":
    # url_for('static', filename='style.css')
    app.run(debug=True)
