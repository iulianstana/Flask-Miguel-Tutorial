import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from config import ADMINS, MAIL_SERVER, MAIL_PORT
from config import MAIL_USERNAME, MAIL_PASSWORD

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# login manager
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

# openID config
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# email handler
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_PASSWORD and MAIL_USERNAME:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT),
                               'no-replay@' + MAIL_SERVER,
                               ADMINS,
                               'micro blog failure',
                               credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)


from app import views, models
