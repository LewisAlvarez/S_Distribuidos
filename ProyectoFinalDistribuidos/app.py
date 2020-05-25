import time

import redis
from flask import Flask
from flask import render_template

app = Flask(__name__)

#@app.route('/')
#def hello():
#    count = get_hit_count()
#    return 'Hello World! I have been seen {} times.\n'.format(count)

posts = []

@app.route("/")
def index():
    return "{} posts".format(len(posts))

@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))
    
@app.route("/templates/signup/")
def show_signup_form():
    return render_template("signup_form.html")