import requests as re
import json

client_id = '7714502'
client_secret = '3BgS8VrAvwQ1PVut3XZv'
redirect = 'http://127.0.0.1:5000/vk-gateway'


def send_request():

    link = f'https://oauth.vk.com/authorize?client_id={client_id}&' \
           f'display=page&' \
           f'redirect_uri={redirect}&' \
           f'scope=email,offline&' \
           f'response_type=code&' \
           f'v=5.124'

    return link


def token(r):
    get_token = 'https://oauth.vk.com/access_token'

    token_param = {

        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect,
        'code': r
    }

    data = json.dumps(token_param)
    response = re.post(url=get_token, data=token_param)
    s = json.loads(response.text.replace('\\', ''))

    return s


def vk_auth(r):
    auth = 'https://api.vk.com/method/users.get'
    auth_param = {
        'fields': 'uid,login,first_name,last_name,screen_name,has_mobile,bdate,photo_max_orig,mail,email',
        'access_token': r,
        'scope': 'email,offline',
        'v': 5.124
    }

    response = re.post(url=auth, data=auth_param)
    s = json.loads(response.content)
    data = s['response'][0]
    return data
