from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def index2():
    return render_template('index2.html')

app.run(host='0.0.0.0', port=5000, debug=True)