from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class myData(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(100))
    user_work=db.Column(db.String(100))
    user_info=db.Column(db.String(300))
    user_img=db.Column(db.String(100))
    _name=db.Column(db.String(100))
    _year=db.Column(db.String(100))
    _phone=db.Column(db.String(100))
    _address=db.Column(db.String(100))
    _email=db.Column(db.String(100))
    _website=db.Column(db.String(100))
    _webdesign=db.Column(db.String(100))
    _uxdesign=db.Column(db.String(100))
    _photoshop=db.Column(db.String(100))
    _phonedesign=db.Column(db.String(100))
    web_info=db.Column(db.String(200))
    ux_info=db.Column(db.String(200))
    photo_info=db.Column(db.String(200))
    phone_info=db.Column(db.String(200))
   


# db.create_all()




class Service(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    s_title=db.Column(db.String(100))
    s_clients=db.Column(db.String(100))
    s_coffe=db.Column(db.String(300))
    s_avards=db.Column(db.String(100))
    s_ideas=db.Column(db.String(100))
    work_first=db.Column(db.String(100))
    work_first_info=db.Column(db.String(100))
    work_second=db.Column(db.String(100))
    work_second_info=db.Column(db.String(100))
    work_third=db.Column(db.String(100))
    work_third_info=db.Column(db.String(100))
    work_fourth=db.Column(db.String(100))
    work_fourth_info=db.Column(db.String(100))
    service_img=db.Column(db.String(100))

# db.create_all()



class Education(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    edu_title=db.Column(db.String(100))
    first_head=db.Column(db.String(100))
    first_year=db.Column(db.String(100))
    first_info=db.Column(db.String(300))
    second_head=db.Column(db.String(100))
    second_year=db.Column(db.String(100))
    second_info=db.Column(db.String(300))
    third_head=db.Column(db.String(100))
    third_year=db.Column(db.String(100))
    third_info=db.Column(db.String(300))
    fourth_head=db.Column(db.String(100))
    fourth_year=db.Column(db.String(100))
    fourth_info=db.Column(db.String(300))

# db.create_all()

class Experience(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    exp_title=db.Column(db.String(100))
    first_head=db.Column(db.String(100))
    first_year=db.Column(db.String(100))
    first_info=db.Column(db.String(300))
    second_head=db.Column(db.String(100))
    second_year=db.Column(db.String(100))
    second_info=db.Column(db.String(300))
    third_head=db.Column(db.String(100))
    third_year=db.Column(db.String(100))
    third_info=db.Column(db.String(300))
    fourth_head=db.Column(db.String(100))
    fourth_year=db.Column(db.String(100))
    fourth_info=db.Column(db.String(300))


# db.create_all()


class Gallery(db.Model):
    s_id = db.Column(db.Integer, primary_key=True)
    img_1=db.Column(db.String(100))
    img_2=db.Column(db.String(100))
    img_3=db.Column(db.String(100))
    img_4=db.Column(db.String(300))
    img_5=db.Column(db.String(100))
    img_6=db.Column(db.String(100))
    img_7=db.Column(db.String(100))
    img_8=db.Column(db.String(100))
    img_9=db.Column(db.String(100))
    img_10=db.Column(db.String(100))
    img_11=db.Column(db.String(100))
    img_12=db.Column(db.String(100))

# db.create_all()

# import app routes
from controllers.app.routes import *

# import admin routes
from controllers.admin.routes import *


if __name__ == '__main__':
    app.run(debug=True)
