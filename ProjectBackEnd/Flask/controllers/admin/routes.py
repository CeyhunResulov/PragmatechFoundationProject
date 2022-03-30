
from run import Education, app,myData,Service,db
from flask import render_template,redirect,request
import os
# admin index route

@app.route('/admin', methods=['GET','POST'])
def admin_index():
    return render_template('admin/index.html')


@app.route('/admin/profil', methods=['GET','POST'])
def admin_profil():
    datalar=myData.query.all()
    if request.method=='POST':
        file=request.files['user_img']
        _img=file.filename
        file.save(os.path.join('static/uploads/',_img))
        s_user_name=request.form['user_name']
        s_user_work=request.form['user_work']
        s_user_info=request.form['user_info']
        s_user_img=_img
        s_name=request.form['_name']
        s_year=request.form['_year']
        s_phone=request.form['_phone']
        s_address=request.form['_address']
        s_email=request.form['_email']
        s_website=request.form['_website']
        s_webdesign=request.form['_webdesign']
        s_uxdesign=request.form['_uxdesign']
        s_photoshop=request.form['_photoshop']
        s_phonedesign=request.form['_phonedesign']
        s_web_info=request.form['web_info']
        s_ux_info=request.form['ux_info']
        s_photo_info=request.form['photo_info']
        s_phone_info=request.form['phone_info']

        data=myData(
            user_name=s_user_name,
            user_work=s_user_work,
            user_info=s_user_info,
            user_img=s_user_img,
            _name=s_name,
            _year=s_year,
            _phone=s_phone,
            _address=s_address,
            _email=s_email,
            _website=s_website,
            _webdesign=s_webdesign,
            _uxdesign=s_uxdesign,
            _photoshop=s_photoshop,
            _phonedesign=s_phonedesign,
            web_info=s_web_info,
            ux_info=s_ux_info,
            photo_info= s_photo_info,
            phone_info=s_phone_info

        )
        db.session.add(data)
        db.session.commit()
        return redirect('/admin/profil')

    return render_template("admin/profil.html",datalar=datalar)

@app.route('/admin/profil/delete/<id>', methods=['GET','POST'])
def admin_profil_delete(id):
    data=myData.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/profil')



# service section


@app.route('/admin/service', methods=['GET','POST'])
def admin_service():
    infos=Service.query.all()
    if request.method=='POST':
        file=request.files['service_img']
        s_service_img=file.filename
        file.save(os.path.join('static/service/',s_service_img))
        sql_title=request.form['s_title']
        sql_clients=request.form['s_clients']
        sql_coffe=request.form['s_coffe']
        sql_avards=request.form['s_avards']
        sql_ideas=request.form['s_ideas']
        sql_work_first=request.form['work_first']
        sql_work_first_info=request.form['work_first_info']
        sql_work_second=request.form['work_second']
        sql_work_second_info=request.form['work_second_info']
        sql_work_third=request.form['work_third']
        sql_work_third_info=request.form['work_third_info']
        sql_work_fourth=request.form['work_fourth']
        sql_work_fourth_info=request.form['work_fourth_info']
        sql_service_img=s_service_img

        info=Service(
            s_title=sql_title,
            s_clients=sql_clients,
            s_coffe=sql_coffe,
            s_avards=sql_avards,
            s_ideas=sql_ideas,
            work_first=sql_work_first,
            work_first_info=sql_work_first_info,
            work_second=sql_work_second,
            work_second_info=sql_work_second_info,
            work_third=sql_work_third,
            work_third_info=sql_work_third_info,
            work_fourth=sql_work_fourth,
            work_fourth_info=sql_work_fourth_info,
            service_img=sql_service_img
    

        )
        db.session.add(info)
        db.session.commit()
        return redirect('/admin/service')

    return render_template("admin/service.html",infos=infos)

@app.route('/admin/service/delete/<id>', methods=['GET','POST'])
def admin_service_delete(id):
    info=Service.query.get(id)
    db.session.delete(info)
    db.session.commit()
    return redirect('/admin/service')



# education section

@app.route('/admin/education', methods=['GET','POST'])
def admin_education():
    edu_infos=Education.query.all()
    if request.method=='POST':
        sql_edu_title=request.form['edu_title']
        sql_first_head=request.form['first_head']
        sql_first_year=request.form['first_year']
        sql_first_info=request.form['first_info']
        sql_second_head=request.form['second_head']
        sql_second_year=request.form['second_year']
        sql_second_info=request.form['second_info']
        sql_third_head=request.form['third_head']
        sql_third_year=request.form['third_year']
        sql_third_info=request.form['third_info']
        sql_fourth_head=request.form['fourth_head']
        sql_fourth_year=request.form['fourth_year']
        sql_fourth_info=request.form['fourth_info']
        edu_info=Education(
            edu_title=sql_edu_title,
            first_head=sql_first_head,
            first_year=sql_first_year,
            first_info=sql_first_info,
            second_head=sql_second_head,
            second_year=sql_second_year,
            second_info=sql_second_info,
            third_head=sql_third_head,
            third_year=sql_third_year,
            third_info=sql_third_info,
            fourth_head=sql_fourth_head,
            fourth_year=sql_fourth_year,
            fourth_info=sql_fourth_info
        )
        db.session.add(edu_info)
        db.session.commit()
        return redirect('/admin/education')

    return render_template("admin/education.html",edu_infos=edu_infos)

@app.route('/admin/education/delete/<id>', methods=['GET','POST'])
def admin_education_delete(id):
    edu_info=Education.query.get(id)
    db.session.delete(edu_info)
    db.session.commit()
    return redirect('/admin/education')


