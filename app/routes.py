from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Doggo'}
	posts = [
		{
			'author': {'username': 'Binta'},
			'body': 'Beautiful day in Ithaca!'
		},
		{
			'author': {'username': 'Milo'},
			'body': 'The Avengers movie was so not so great!'
		}
	]
	return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/boot_test')
def boot_test():
	return render_template('boot_test.html')