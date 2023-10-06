from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask_wtf import form
from wtforms.fields import TextField
from wtforms.fields import passwordField
from wtforms.fields import sumbitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'i_love_pizza'

class UserFORm(form):
    username = TextField("Name of the User :")
    password = passwordField("user password:")
    sumbit = sumbitField("ENTER CREDENTIALS:")


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = UserForm()
    if request.method == 'PORT':
        return render_template('display.html')
    return render_template('upload.html', form = form)

    


if __name__ == '__main__':
    app.run(debug="True, port=8080")