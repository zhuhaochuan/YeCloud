#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import request
from flask import render_template,redirect,url_for
from ORMTest import  DBSession,Userinfo
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 创建DBSession类型:
    session = DBSession()
    # 需要从request对象读取表单内容：
    res = session.query(Userinfo).filter(Userinfo.name==request.form['username'] , Userinfo.password==request.form['password']).all()
    if len(res)==0:
        session.close()
        return render_template('login.html')
    else:
        session.close()
        return redirect(url_for('upload'))


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath,'static/uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()