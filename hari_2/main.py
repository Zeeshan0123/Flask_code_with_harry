from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from markupsafe import escape
from datetime import datetime
import json

with open("./templates/config.json","r") as c:
  params = json.load(c)["params"]
  
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
db = SQLAlchemy(app)
# initialize the app with the extension
# db.init_app(app)

class Contacts(db.Model):
    # Make sure use words that are used in your real database
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=False,nullable=False)
    phone_no = db.Column(db.String(12),unique=True,nullable=False)
    msg = db.Column(db.Text,unique=True,nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(20),unique=True,nullable=False)


@app.route("/")
def home():
  return render_template('index.html',params=params)

@app.route("/contact",methods=['GET','POST'])
def contact():
  if(request.method=='POST'):
    """Add entries in the database"""
    name = request.form.get('name')
    phone_number = request.form.get('phone')  # This phone is actually a name used in contact.html
    message = request.form.get('message')
    email = request.form.get('email')
    entry = Contacts(name=name,phone_no=phone_number,msg=message,email=email)
    
    db.session.add(entry)
    db.session.commit()
  return render_template('contact.html',params=params)

@app.route("/about")
def about():
  return render_template('about.html',params=params)

@app.route("/post")
def post():
  return render_template('post.html',params=params)

app.run()