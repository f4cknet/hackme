from models import db,redis_client
from models.user import User
from flask import redirect,url_for,session
from datetime import datetime

def identify(openid):
    user = User.query.filter_by(openId=openid).first()
    if not user.idcard_verify:
        return {"code":40001,"msg":"not identify"}
    return {"code":40000,"msg":"identify"}

def login_init():
    if not session.get('openid'):
        return redirect(url_for('weixin.oauth'))
    else:
        openid = session.get('openid')
        q_user = User.query.filter_by(openId=openid).first()
        if not q_user:
            userid = str(uuid1()).replace("-",'')
            user = User(id=userid,openId=openid)
            db.session.add(user)
            db.session.commit()
        timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        redis_client.lpush(f"loginr_{openid}",timenow)
        return {"code":20001,"msg":"hello:"+session.get('openid')}