# explore-python-react

Purpose is to explore Python Flask and React integration


# Setup App:
- create app folder
- `cd` app folder
- `git int` 

# Server side with Flask 

Setup:
- create app folder
- `cd` app folder
- `git int` 
- `poetry new server`
- `poetry add flask`
- create `app.py` file inside server
- `poetry add python-dotenv`
- create `.flaskenv` with `FLASK_APP=server`

Run:

`poetry run flask run`

Check:

`http://localhost:5000`

<br/>

# Client side with React 

Setup:
- `npx create-react-app client`

Run:

`yarn start`

Check:

`http://localhost:3000/app`


# FLASK_ENV

With FLASK_ENV:
- `=production` deployable flask application serving statically built React assets 
- `=development` hot-reloading workspace that incrementally rebuilds changes to both React and Flask applications.