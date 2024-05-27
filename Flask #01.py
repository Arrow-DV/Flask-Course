# Import Flask Module
from flask import Flask 
# Init The Main App
app = Flask(__name__)
# Set App Routes
# @variable_name.route('address')
@app.route('/')
@app.route('/home')
def index():
    return '<h1>This Is HomePage</h1>'

@app.route('/info')
@app.route('/about')
def about():
    return 'This Is About Page'
# Run The Server With Debug Mode
app.run(debug=True)
