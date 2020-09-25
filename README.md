# Flask + CAS Template

A barebones Flask app using CAS for authentication.

## Features
- Flask
- CAS authentication
- Bootstrap
    - Template with navbar and footer included
    - Other utils like macros and flash messages included

## Setup

1. Create a repo from this template and clone it locally
2. Activate the [pipenv](https://github.com/pypa/pipenv) environment with `$ pipenv shell`
3. Install packages with `$ pipenv install`
4. Create the `.env` file in the root folder with the keys from `.env.example`

## Running
Run the app in development mode with
```bash
$ flask run
```
It will automatically restart when in development mode if you change files.

## Deployment
Deployment is easiest on Heroku with the Procfile included in this template. Create a Heroku app from the Heroku Dashboard online. For more details see [here](https://devcenter.heroku.com/articles/git).

### Connect Heroku app (once)
```bash
$ heroku git:remote -a <heroku-app-name>
```

### Deploy to Heroku
```bash
$ git push heroku master
```

## Screenshots
![index](https://snipboard.io/qFNKIE.jpg)