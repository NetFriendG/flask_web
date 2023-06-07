from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello gm'


if __name__ == '__main__':
    app.run(host='127.0.0.1',prot=10080)