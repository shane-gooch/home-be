from flask import Flask

app = Flask(__name__)


@app.route('/login')
def loginIn():
    pass


@app.route('/userInfo')
def getUserInfo():
    pass


if __name__ == "__main__":
    app.run(debug=True)
