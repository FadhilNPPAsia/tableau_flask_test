from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello, world !"

@app.route('/dashboard_test')
def dashboard_test():
    return render_template('dashboard_test.html')