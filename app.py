import os
from flask import Flask, abort, flash, g, session, request, render_template, redirect, url_for
from flask_cas import CAS, login_required
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException

# Loads any variables from the .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Initialize CAS authentication on the /cas endpoint
# Adds the /cas/login and /cas/logout routes
cas = CAS(app, '/cas')

# This must be a RANDOM string you generate once and keep secret
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# Used in templates
app.config['APP_TITLE'] = 'Flask + CAS'

# Must be set to this to use RPI CAS
app.config['CAS_SERVER'] = 'https://cas-auth.rpi.edu/cas'

# What route to go to after logging in
app.config['CAS_AFTER_LOGIN'] = 'index'


@app.before_request
def before_request():
    '''Runs before every request.'''

    # Everything added to g can be accessed during the request
    g.logged_in = cas.username is not None


@app.context_processor
def add_template_locals():
    '''Add values to be available to every rendered template.'''

    # Add keys here
    return {
        'logged_in': g.logged_in,
        'username': cas.username
    }


@app.route('/')
def index():
    '''The homepage.'''
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
@login_required
def form():
    '''Sample form route.'''

    if request.method == 'GET':
        # Render form page on GET request
        return render_template('form.html')
    else:
        # Grab form values on POST request
        if 'name' in request.form and request.form['name'] != '':
            name = request.form['name']
            flash('Hello, ' + name, 'info')
        else:
            abort(400)

        return redirect(url_for('form'))


@app.route('/about')
def about():
    '''The about page.'''
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found():
    '''Render 404 page.'''
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def handle_exception(e):
    '''Handles all other exceptions.'''

    # Handle HTTP errors
    if isinstance(e, HTTPException):
        return render_template('error.html', error=e), e.code

    # Handle non-HTTP errors
    app.logger.exception(e)

    # Hide error details in production
    if app.env == 'production':
        e = 'Something went wrong... Please try again later.'

    return render_template("error.html", error=e), 500
