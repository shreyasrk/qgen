from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Shreyas'}
    title = 'QGen: Home'
    posts = [{'author': {'nickname': 'Shreyas'}, 'body': 'The first post.'},
        {'author': {'nickname': 'Rajeev'}, 'body': 'The second post.'},
        {'author': {'nickname': 'Kulkarni'}, 'body': 'The third post.'}]
    return render_template('index.html', title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login required for openID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
    	title='Sign In', 
    	form=form,
        providers = app.config['OPENID_PROVIDERS'])
