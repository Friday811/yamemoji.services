from flask import Flask

app = Flask(__name__)


@app.route('/')
def yam():
    return '🍠'

@app.route('/<count>')
def yams(count):
    return count * '🍠'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8635)
