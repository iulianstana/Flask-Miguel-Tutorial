from flask import render_template
from app import app


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
