# -*- coding: utf-8 -*-
from flask import render_template, redirect, request
from app import app
from app.auth import vk


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/vk-gateway')
def gateway():
    """

    :return:
    """
    code = request.args.get('code')
    data = vk.token(r=code)

    user_data = vk.vk_auth(data['access_token'])
    first_name = user_data['first_name']
    last_name =user_data['last_name']
    avatar = user_data['photo_max_orig']
    nickname = user_data['screen_name']

    user = {
        'nickname': nickname,
        'first_name': first_name,
        'last_name': last_name,
        'avatar': avatar
    }
    return render_template('auth.html', user=user)


@app.route('/vk-auth')
def authVK():
    link = vk.send_request()
    return redirect(link, code=301)
