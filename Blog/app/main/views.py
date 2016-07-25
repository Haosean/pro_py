from flask import render_template, session, url_for, redirect, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm


# @main.route('/')
# def index():
#     render_template('index.html')
@main.route('/')
def index():
    return render_template('index.html')

# from flask import render_template
# from . import main
