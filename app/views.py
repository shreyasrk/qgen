from flask import render_template, flash, redirect, request
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Shreyas'}
    title = 'QGen: Home'
    return render_template('index.html', title=title, user=user)

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

@app.route('/search')
def search():
    inp_1 = request.args.get('inp_1', '')
    inp_2 = request.args.get('inp_2', '')
    inp_3 = request.args.get('inp_3', '')

    return "Got the Inputs! Call your function here.."