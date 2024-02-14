from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def helo_world():
  return "<p>Hi! Welcome to flask Zeeshan</p>"

@app.route("/farhan")
def helo_farhan():
  return "<p>Hi! Welcome to flask Farhan</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
  
@app.route("/post/<int:post_id>")
def show_post(post_id):
  return f'Post {post_id}'

@app.route("/alert")
def warning():
  return '<script> alert("bad") </script>'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
  # show the subpath after /path/  like string but also accept slashes
  return f'Subpath {escape(subpath)}'

@app.route('/index')
@app.route('/index/<name>')
def show_index(name=None):
  return render_template('index.html',name=name)
  
  

app.run(debug=True)