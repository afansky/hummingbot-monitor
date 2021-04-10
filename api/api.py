from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def store():
    print("got a request")
    return "YO"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')