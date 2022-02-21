from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class myData(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    user_name=db.column(db.String(100))
    user_work=db.column(db.String(100))
    user_info=db.column(db.String(300))
    user_img=db.column(db.String(100))
# db.create_all()

# import app routes
from controllers.app.routes import *

# import admin routes
from controllers.admin.routes import *


if __name__ == '__main__':
    app.run(debug=True)
