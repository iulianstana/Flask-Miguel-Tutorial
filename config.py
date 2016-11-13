# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you will never guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# SQLALCHEMY_TRACK_MODIFICATIONS = False  # affects whoose

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 2525
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['iulianstana@yahoo.com']

# pagination
POSTS_PER_PAGE = 5

# Whoosh configuration
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_TARGETS = 50

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español',
    'ro': 'Romanian'
}
