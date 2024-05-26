# Import Main Flask Class
from flask import Flask
# Init The App
app = Flask(__name__) 
# Set Routes
@app.route('/')
def index():
  return '<h1>Home</h1>'
