from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL  

# @app.errorhandler(404)
# def pageNotFound(e):
    # return render_template('notfound.html')
    # return f'Error:{e}' 

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('index.html')

@app.route('/qualifish')
def qualifish(): 
    return render_template('qualifish.html')

@app.route('/wiims')
def wiims(): 
    return render_template('wiims.html')
 
@app.route('/afms')
def afms(): 
    return render_template('afms.html')

@app.route('/thinktaps')
def thinktaps(): 
    return render_template('thinktaps.html')

@app.route('/about')
def about(): 
    return render_template('about.html')

@app.route('/navbar')
def navbar(): 
    return render_template('navbar.html')

if __name__ == "__main__":
    app.run(debug=True)

