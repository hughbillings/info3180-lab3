from flask import Flask
from flask_mail import Mail



app = Flask(__name__)


app.config['SECRET_KEY']= 'enter some random passphrase'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']= '2525'
app.config['MAIL_USERNAME']='17767a33e50f1b'
app.config['MAIL_PASSWORD']='8233f14ea2fb37'
mail = Mail(app)

from app import views