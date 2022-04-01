from run import Education, Gallery, app,myData,db,Service,Experience
from flask import render_template,redirect,request

# app index route

@app.route('/', methods=['GET','POST'])
def app_index():
    datalar=myData.query.all()
    infos=Service.query.all()
    edu_infos=Education.query.all()
    exp_infos=Experience.query.all()
    gallerys=Gallery.query.all()
    return render_template('app/index.html',datalar=datalar,infos=infos,edu_infos=edu_infos,exp_infos=exp_infos,gallerys=gallerys)



