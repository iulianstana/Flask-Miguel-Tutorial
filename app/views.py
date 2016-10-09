from flask import render_template, redirect
from flask import session, url_for, g

from flask_login import current_user

from app import app
from app import lm
from app import oid

from .models import User
from .forms import LoginForm


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Iulian'}

    posts = [
        {
            'author': {'nickname': 'Nuca'},
            'body': 'Do a cake with Worm!'
        },
        {
            'author': {'nickname': 'Worm'},
            'body': 'Avreage time was 1 hour'
        }
    ]

    return render_template('index.html',
                            user=user,
                            posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))