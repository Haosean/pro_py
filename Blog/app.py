from flask import Flask,render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return 'Blog'

@app.route('/user/<name1>')
def user(name1):
    return render_template('user.html',name2=name1)


if __name__ == '__main__':
    manager.run()
