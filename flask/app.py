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
    '''
    The home route.
    '''
    return render_template('index.html', logged_in=cas.username is not None, username=cas.username)
