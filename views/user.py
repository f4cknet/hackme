from flask import Blueprint,request,session,render_template,jsonify,url_for,redirect
from lib.loginservice import verify_user
from models.admin import Notice
from models.user import User
from models import db,redis_client
from datetime import datetime
from lib.baseauth import identify,login_init
from uuid import uuid1




user_blue = Blueprint('user',__name__,url_prefix='/user')

@user_blue.route('/notice',methods=["GET","POST"])
def index():
    result = Notice.query.get(1)
    if not result:
        content = "请不要轻易相信陌生人，特别涉及到钱财"
    else:
        content = result.content
    return {"code":20001,"data":content}


@user_blue.route('/list',methods=["GET","POST"])
def user_list():
    if request.method=="POST":
        data = request.json
        order_by = data.get('order_by')
        if order_by==0:
            column = "score"
        elif order_by==1:
            column = "login_time"
        elif order_by==2:
            column = "create_time"
        elif order_by == 3:
            column = "like_favorite"
        page = data.get('page')
        # User.query.order_by(order).paginate(page,per_page=20)