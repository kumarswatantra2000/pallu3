from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return("This is the suman gengopadhay's flask application")

@app.route('/about')
def about():
    return("This is the about pages of suman gengopadhay")

if __name__ == '__main__':
    app.run(debug = True, port=5000)