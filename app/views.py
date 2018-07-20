from flask import render_template, request, redirect, url_for, jsonify
from app import app
from . nlp import nlp_process
from . models import User, Post, db
from datetime import datetime



@app.route('/')
@app.route('/index')
def index(current_task=None):
	user = {'username': 'Doggo'}
	if current_task:
		print(current_task)
	try:
		posts = Post.query.filter_by(author='user').all()
	except:
		posts = {}    

	return render_template('index.html', title="Home", user=user, posts=posts, time=datetime.now(), task=current_task)


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

    task = nlp_process.apply_async()
    print(task.id)

    return index(task.id)

@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = nlp_process.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)