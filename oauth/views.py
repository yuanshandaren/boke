from django.http import HttpResponseRedirect
import urllib.parse
import urllib.request
import collections
import json
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
# Create your views here.

APP_ID = '****'
APP_SECRET = "****"
REDIRECT_URI = 'http://blog.dev2.gzqichang.com/accounts/weixin/login/done/'

def weixin_login(request):
    d = collections.OrderedDict()
    d['appid'] = APP_ID
    d['redirect_uri'] = REDIRECT_URI
    d['response_type'] = 'code'
    d['scope'] =  'snsapi_login'
    d['state'] =  'no'
    weixin_auth_url = '%s?%s' % ('https://open.weixin.qq.com/connect/qrconnect',
                             urllib.parse.urlencode(d))
    return HttpResponseRedirect(weixin_auth_url)

def weixin_auth(request):
    code = request.GET.get('code')
    data = get_access_token(code)
    access_token = data['access_token']
    openid = data['openid']
    refresh_token = data['refresh_token']
    if not check_access_token(access_token, openid):
        data1 = get_refresh_token(refresh_token)
        access_token = data1['access_token']
    id = get_user_info(access_token, openid, request)
    return HttpResponseRedirect(reverse('personal', args=(id,)))

def get_access_token(code):                                  
    auth_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?'
    d = collections.OrderedDict()
    d['appid'] = APP_ID
    d['secret'] = APP_SECRET
    d['code'] = code
    d['grant_type'] = 'authorization_code'
    body = urllib.parse.urlencode(d)
    headers = {'Accept': 'application/json'}
    body1 = body.encode('utf-8')
    req = urllib.request.Request(auth_url, body1, headers)
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    return data

def get_user_info(access_token, openid, request):
    if access_token:
        url = 'https://api.weixin.qq.com/sns/userinfo?'
        d = collections.OrderedDict()
        d['access_token'] = access_token
        d['openid'] = openid
        d['lang'] = 'zh_CN'
        body = urllib.parse.urlencode(d)
        headers = {'Accept': 'application/json'}
        body1 = body.encode('utf-8')
        req = urllib.request.Request(url, body1, headers)
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read().decode('utf-8'))

        username = data['nickname']
        unionID = data['unionid']
        email = '@qq.com'
        password = '411658758'
        try:
            user = User.objects.get(username=username)
        except:
            user = User.objects.create_user(username, email, password)
            user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return user.id

def check_access_token(access_token, openid):
    url = 'https://api.weixin.qq.com/sns/auth?'
    d = collections.OrderedDict()
    d['access_token'] = access_token
    d['openid'] = openid
    body = urllib.parse.urlencode(d)
    headers = {'Accept': 'application/json'}
    body1 = body.encode('utf-8')
    req = urllib.request.Request(url, body1, headers)
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    if data['errmsg'] == 'ok':
        return True
    else:
        return False

def get_refresh_token(refresh_token):
    url = 'https://api.weixin.qq.com/sns/oauth2/refresh_token?'
    d = collections.OrderedDict()
    d['appid'] = APP_ID
    d['grant_type'] = 'refresh_token'
    d['refresh_token'] = refresh_token
    body = urllib.parse.urlencode(d)
    headers = {'Accept': 'application/json'}
    body1 = body.encode('utf-8')
    req = urllib.request.Request(url, body1, headers)
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    return data





