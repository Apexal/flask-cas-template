# Flask + CAS Template

A barebones Flask app using CAS for authentication.

## Development

### Activate environment
```bash
$ pipenv shell
```

### Dependencies
This template uses `pipenv` to manage dependencies. Install new dependencies with `$ pipenv install <package-name>` and reinstall all listed dependencies with `$ pipenv install`. Read more about pipenv [here](https://github.com/pypa/pipenv).

### Environment Variables
Create a `.env` file based on `.env.example` and change the placeholder values. The app loads all variables in `.env` into `os.environ`.

### Running
Run the app in development mode with
```bash
$ flask run
```

## Deployment
Deployment is easiest on Heroku with the Procfile included in this template. Create a Heroku app from the Heroku Dashboard online.

### Connect Heroku app (once)
```bash
$ heroku git:remote -a <heroku-app-name>
```

### Deploy to Heroku
```bash
$ git push heroku
```