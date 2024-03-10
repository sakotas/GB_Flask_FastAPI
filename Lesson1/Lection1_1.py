from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return 'Привет, ' + name.capitalize() + '!'


if __name__ == '__main__':
    app.run()
