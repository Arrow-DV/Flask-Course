from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    # n % 2 == 0  | Even
    numbers = [1,2,3,4,5,6,7,8,9,10]
    return render_template('index.html',numbers=numbers)

app.run(debug=True)