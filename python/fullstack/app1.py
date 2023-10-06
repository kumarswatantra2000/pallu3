from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route('/', method = ['GET', 'POST'])
def index():
    if request.wethod == 'POST':
        from = request.from
        name = from['my_name']
        return render_template('index.html', data = name)
    return render_template('swatantra.html')
if __name__ == '__main__':
    app.run(debug=True. port=5000)