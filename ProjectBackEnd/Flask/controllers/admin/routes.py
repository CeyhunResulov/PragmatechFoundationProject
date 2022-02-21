from run import app,myData,db 
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

        data=myData(
            user_name=s_user_name,
            user_work=s_user_work,
            user_info=s_user_info,
            user_img=s_user_img
        )
        db.session.add(data)
        db.session.commit()
        return redirect('/admin/profil')

    return render_template("admin/profil.html",datalar=datalar)