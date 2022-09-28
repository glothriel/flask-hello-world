from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        "Hello": "world2"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
