from flask import Blueprint,request,redirect,session,url_for,Response
import hashlib,requests
from models.user import User
from models import db
import json
from uuid import uuid1
from datetime import datetime

weixin_blue = Blueprint('weixin',__name__,url_prefix='/weixin')

token = "WXPPOsXJj20QVPJ1oUqzJp2FjpJQFEOe"
APPID = "wxe2f3d97857f8cbc8"
SECRET = "11108564cb51cfa19453182b64a167e0"

@weixin_blue.route('/checksign')
def checksign():
    nonce = request.args.get('nonce')
    timestamp = request.args.get('timestamp')
    sign = request.args.get('signature')

    tmp = [nonce,timestamp,token]
    print(tmp)
    tmp.sort()
    data = ''.join(tmp)
    tmpsign = hashlib.sha1(data.encode('utf-8')).hexdigest()
    if tmpsign == sign:
        return request.args.get('echostr')
    else:
        return False

# @weixin_blue.route('/oauth')
# def oauth():
#     redirect_url = "https%3A%2F%2Fweixinapi.itner.net%2Fweixin%2Fcallback"
#     url = f"https://open.weixin.qq.com/connect/oauth2/authorize?appid={APPID}&redirect_uri={redirect_url}&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
#     return request(url)

@weixin_blue.route('/login',methods=['POST'])
def login():
    code = request.json.get('code')
    url = f"https://api.weixin.qq.com/sns/oauth2/access_token?appid={APPID}&secret={SECRET}&code={code}&grant_type=authorization_code"
    req = requests.get(url)
    data = json.loads(req.text)
    print(data)
    openid = data.get('openid')
    result = User.query.filter_by(openId=openid).first()
    if not result:
        userid = str(uuid1()).replace('-','')
        user = User(id=userid,openId=openid)
        db.session.add(user)
        db.session.commit()
    token = hashlib.md5((openid+str(datetime.now())).encode('utf-8')).hexdigest()
    return {"code":20001,"token":token}


