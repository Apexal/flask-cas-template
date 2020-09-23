import os
from flask import Flask, flash, g, session, request, render_template, redirect, url_for
from flask_cas import CAS, login_required, logout
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException

# Loads any variables from the .env file
load_dotenv()

app = Flask(__name__)
cas = CAS(app, '/cas')

# This must be a RANDOM string you generate once and keep secret
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# Must be set to this to use RPI CAS
app.config['CAS_SERVER'] = 'https://cas-auth.rpi.edu/cas'

# What route to go to after logging in
app.config['CAS_AFTER_LOGIN'] = 'index'


@app.route('/')
def index():
    '''The homepage.'''
    return render_template('index.html', logged_in=cas.username is not None, username=cas.username)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        if 'name' in request.form and request.form['name'] != '':
            name = request.form['name']
            flash('Hello, ' + name)
        else:
            flash('You didn\'t give a name!', 'error')

        return redirect(url_for('form'))


@app.route('/about')
def about():
    '''The about page.'''
    return render_template('about.html')


@app.errorhandler(Exception)
def handle_exception(e):
    '''Handles non-HTTP exceptions.'''
    # Pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    app.logger.exception(e)

    # Hide error in production
    if app.env == 'production':
        e = 'Something went wrong... Please try again later.'

    return render_template("error.html", error=e), 500
