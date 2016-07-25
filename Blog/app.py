from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')



if __name__ == '__main__':
    manager.run()
