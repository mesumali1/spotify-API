from flask import Flask, request
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'


if __name__ == '__main__':
 app.run()