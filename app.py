import os
from flask import Flask, g, session, request, render_template, redirect, url_for
from flask_cas import CAS, login_required, logout
from dotenv import load_dotenv

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


@app.route('/form', methods=['POST'])
def form():
    if 'name' in request.form and request.form['name'] != '':
        name = request.form['name']
        return f'Hello, {name}'
    else:
        return 'You gave me no name!'


@app.route('/about')
def about():
    '''The about page.'''
    return render_template('about.html')


@app.errorhandler(Exception)
def handle_error(e):
    '''Generic error handler that renders error template with message.'''
    app.logger.error('An error occurred:')
    app.logger.exception(e)

    # Hide error in production
    error = e
    if app.env == 'production':
        error = 'Something went wrong... Please try again later.'

    return render_template('error.html', error=error), 500
