from flask import render_template, request, redirect, url_for
from app import app
from . nlp import nlp_process
from . models import User, Post, db
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Doggo'}
	try:
		posts = Post.query.filter_by(author='user').all()
	except:
		posts = {}
	
	return render_template('index.html', title="Home", user=user, posts=posts, time=datetime.now())


@app.route('/boot_test')
def boot_test():
	return render_template('boot_test.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    # author = request.form['author']
    # date_posted = request.form['date_posted']
    content = request.form['content']
    author = "user"

    post = Post(title=title, author=author, date_posted=datetime.now(), content=content)

    db.session.add(post)
    db.session.commit()
    task = nlp_process.delay()

    return redirect(url_for('index'))