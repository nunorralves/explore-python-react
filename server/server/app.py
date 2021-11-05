from os import environ
from flask import Flask, request
from requests import get

IS_DEV = environ["FLASK_ENV"] == "development"
WEBPACK_DEV_SERVER_HOST = "http://localhost:3000"

app = Flask(__name__)

# In Flask, during development, we can pass static asset requests on to Webpack Dev Server, 
# using a simple reverse proxy implementation.
def proxy(host, path):
  print('HOST: ' + host)
  print('PATH: ' + path)
  print('ALL: ' + f"{host}{path}")
  response = get(f"{host}{path}")
  excluded_headers = [
    "content-encoding",
    "content-length",
    "transfer-encoding",
    "connection",
  ]
  headers = {
    name: value
    for name, value in response.raw.headers.items()
    if name.lower() not in excluded_headers
  }
  return (response.content, response.status_code, headers)


@app.route('/')
def getRoot():
  return "Welcome!"

@app.route("/app/", defaults={"path": "index.html"})
@app.route("/app/<path:path>")
def getApp(path):
  if IS_DEV:
    return proxy(WEBPACK_DEV_SERVER_HOST, request.path)
  return app.send_static_file(path)

