from flask import request, Flask
import json

app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Welcome user.\napp1 is running on python environment'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')