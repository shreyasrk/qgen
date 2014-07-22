from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Shreyas'}
	title = 'QGen: Home'
	posts = [{'author': {'nickname': 'Shreyas'}, 'body': 'The first post.'},
			{'author': {'nickname': 'Rajeev'}, 'body': 'The second post.'},
			{'author': {'nickname': 'Kulkarni'}, 'body': 'The third post.'}]
	return render_template('index.html', title=title, user=user, posts=posts)


