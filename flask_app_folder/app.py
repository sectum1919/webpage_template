'''
Author: sectum1919 1048186774@qq.com
Date: 2022-08-17 17:42:46
LastEditors: sectum1919 1048186774@qq.com
LastEditTime: 2022-08-18 11:19:40
Description: 

'''
import json
from flask import Flask, render_template, request, g, redirect, session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib import sqla
from flask_basicauth import BasicAuth
from flask_apscheduler import APScheduler
from werkzeug.exceptions import HTTPException, Response
import sqlite3
import random
import re
import time
import datetime

DATABASE = 'static/test.db'

app = Flask(__name__)
# for session / cookie
app.secret_key = 'fasndlkjfhqakdwsjfnakjs,vnakwjeh'
# 中文显示
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
# admin账号密码
app.config['BASIC_AUTH_USERNAME'] = 'csltroot'
app.config['BASIC_AUTH_PASSWORD'] = 'cslt@tsinghua.1303'
# 使用BasicAuth做后台的权限验证
basic_auth = BasicAuth(app)


# 定时任务
def scheduler():
    pass
# 任务配置类
class APSchedulerJobConfig(object):
    JOBS = [{
        'id': 'scheduler',
        'func': scheduler,
        'args': None,
        'trigger': {
            'type': 'cron',  # cron类型
            'day_of_week': "0-6",  # 每周一到周日
            'hour': '8',  # 的第8小时
            'minute': '0'  # 的第0分钟
        }
    }]
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_ECHO = True
# 设置定时任务
app.config.from_object(APSchedulerJobConfig())
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

"""
POST Route
"""
# upload methods
@app.route('/upload/information', methods=['POST'])
def upload_information():
    data = request.get_data().decode("UTF-8")
    print(data)
    with open('./static/information.txt', 'a') as fp:
        fp.write(data + '\n')
    return 'success'

@app.route('/upload/image', methods=['POST'])
def post_image_file():
    print(request.url)
    file = request.files['filepond']
    print(file.filename)
    file.save(f"./static/media/image/{file.filename}")
    return 'accept image file'
    
@app.route('/upload/audio', methods=['POST'])
def post_audio_file():
    print(request.url)
    file = request.files['filepond']
    print(file.filename)
    file.save(f"./static/media/audio/{file.filename}")
    return 'accept audio file'
    
@app.route('/upload/video', methods=['POST'])
def post_video_file():
    print(request.url)
    file = request.files['filepond']
    print(file.filename)
    file.save(f"./static/media/video/{file.filename}")
    return 'accept video file'
"""
login & register
"""
# 正则判断是否由 0~9, a~z, A~Z, _ 组成
def validStr(s):
    return re.match("^[a-z0-9A-Z_]{2,10}$", s)
# login
# GET method: get html
# POST method: send username and password to verify
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', message='用户系统尚未实现，请随便填写')
    elif request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        if not (validStr(userid) and validStr(password)):
            return render_template(
                'login.html',
                message = '账户和密码由 2~10个 大小写英文字母、数字、下划线组成',
            )
        session['username'] = userid
        return redirect('/')
# reginster
# GET method: get html
# POST method: send username and password to verify
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', message='用户系统尚未实现，请随便填写')
    elif request.method == 'POST':
        print("register")
        userid = request.form['userid']
        password = request.form['password']
        password2 = request.form['password2']
        telphone = request.form['telphone']
        if password != password2:
            return render_template('register.html', message='两次密码不一致')
        if len(userid) == 0 or len(password) == 0:
            return render_template('register.html', message='请填写用户名和密码')
        if not (validStr(userid) and validStr(password)):
            return render_template('register.html', message='账户和密码由 2~10个 大小写英文字母、数字、下划线组成')
        session['username'] = userid
        return redirect('/')
"""
Page Route
"""
# uploader demo page
@app.route('/upload', methods=['GET', 'POST'])
def upload_index():
    return render_template("file_uploader.html")
# empty demo page
@app.route('/empty', methods=['GET', 'POST'])
def empty_page():
    return render_template("empty_page.html")
# audio preview page
@app.route('/audio_preview', methods=['GET', 'POST'])
def audio_preview():
    return render_template("audio_preview.html")
# index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect('/login')
    return render_template(
        "index.html",
        username=session['username'],
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=36922, debug=True)