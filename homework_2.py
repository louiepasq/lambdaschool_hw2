from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'April 10 1981'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name

@app.route('/add/<first>/<second>')
def add(first,second):
    try:
        sum = str(int(first) + int(second))
    except:
        sum = 'At least one of the summands was not a number'
    return sum

@app.route('/multiply/<first>/<second>')
def multiply(first,second):
    try:
        product = str(int(first)*int(second))
    except:
        product = 'At least one of the factors was not a number'
    return product

@app.route('/subtract/<first>/<second>')
def subtract(first,second):
    try:
        difference = str(int(first) - int(second))
    except:
        difference = 'The minuend or subtrahend was not a number'
    return difference

@app.route('/favoritefoods')
def favoritefoods():
    favfoods = ['pizza','hot peppers','angel hair pasta with sauce']
    return jsonify(favfoods)
