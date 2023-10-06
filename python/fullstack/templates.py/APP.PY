# python flask file upload
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)






if __name__ == 'main':
    app.run(debug=True, port=5000)
