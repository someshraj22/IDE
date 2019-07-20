from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://user1:Password@1234@192.168.99.1/python_ide'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['WHOOSH_BASE']='whoosh'
db = SQLAlchemy(app)
from python_ide.views.index import bp as index
from python_ide.views.ide import bp as ide
from python_ide.views.save import bp as save
from python_ide.views.search import bp as search
app.register_blueprint(index)
app.register_blueprint(ide)
app.register_blueprint(save)
app.register_blueprint(search)

