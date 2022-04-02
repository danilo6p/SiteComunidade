from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




basedir = os.path.abspath(os.path.dirname(__file__)
app = Flask(__name__)

app.config[‘SQLALCHEMY_DATABASE_URI’] =\‘sqlite:///’ + os.path.join(basedir, ‘todo.sqlite’)
app.config[‘SQLALCHEMY_TRACK_MODIFICATIONS’] =  False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
id = db.Column(db.Integer, primary_key=True)
description = db.Column(db.String(200), nullalble=False)
date_created = db.Column(db.DateTime, default=datetime.utcnow)
def __repr__(self):
return f“Task: #{self.id}, description: {self.description}”

Bootstrap(app)

@app.route("/")
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

