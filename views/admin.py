from flask import Blueprint,request,session,render_template,redirect,url_for
from lib.authservice import admin_auth
from lib.loginservice import *
from models.admin import *
from models import db

admin_blue = Blueprint('admin',__name__,url_prefix='/admin')


@admin_blue.route('/register_form',methods=["POST","GET"])
def admin_register_form():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if password != password2:
            return {"msg":"两次密码不对"}
        try:
            admin = Admin(username=username,password=password)
            db.session.add(admin)
            db.session.commit()
            return redirect(url_for('admin.admin_login_form'))
        except Exception as e:
            db.session.rollback()
            raise e
            # return {"code":40001,"msg":"该用户已注册"}
    return render_template("admin_register.html")

@admin_blue.route('/login_form',methods=["POST","GET"])
def admin_login_form():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get('password')
        auth = verify_admin(username,password)
        if auth:
            session['uid'] = auth.id
            session["username"] = username
            session["role"] = 'admin'
            return redirect(url_for('admin.admin_index'))
        else:
            return "login failed"
    return render_template("admin_login.html")

@admin_blue.route('/login',methods=["POST","GET"])
def admin_login():
    if request.method == "POST":
        data = request.json
        username = data.get("username")
        password = data.get('password')
        auth = verify_admin(username,password)
        if auth:
            session['uid'] = auth.id
            session["username"] = username
            session["role"] = 'admin'
            return {"code":10001,"msg":"login success"}
        else:
            return "login failed"
    return render_template("admin_login.html")


@admin_blue.route('/index',methods=["GET"])
@admin_auth
def admin_index():
    return {"code":20001,"msgr":"hello"+session.get('username')}

@admin_blue.route('/add_admin',methods=["POST"])
@admin_auth
def add_admin():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    try:
        admin = Admin(username=username,password=password)
        db.session.add(admin)
        db.session.commit()
        return {"msg":"success"}
    except Exception as e:
        print(e)

@admin_blue.route('/add_admin_form',methods=["POST","GET"])
@admin_auth
def add_admin_form():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            admin = Admin(username=username,password=password)
            db.session.add(admin)
            db.session.commit()
            return {"msg":"success"}
        except Exception as e:
            print(e)
    return render_template("add_admin_form.html")

@admin_blue.route('/del_user',methods=["POST"])
@admin_auth
def del_user():
    data = request.json
    username = data.get('username')
    try:
        db.session.query(Admin).filter_by(username=username).delete()
        db.session.commit()
        return {"msg":"delete user success"}
    except Exception as e:
        print(e)

# @admin_blue.route('/generate_recharge code',methods=['GET'])
# @admin_auth
# def generate_recharge_code():
#     type = request.args["type"] or ''
#     code = random.randint(100000, 999999)
#     items = {"1":10,"2":20,"3":30,"4":40,"5":50}
#     if type in items.keys():
#         try:
#             flag = Flag(code=code,isused=False,price=items.get(type))
#             db.session.add(flag)
#             db.session.commit()
#             return jsonify({"code": code})
#         except Exception as e:
#             logging.error(e)
#             raise e
#     else:
#         return jsonify({"code":40001,"msg":"failed"})

@admin_blue.route('/good_add_form',methods=["GET","POST"])
@admin_auth
def good_add_form():
    if request.method == "POST":
        title = request.form.get('title')
        price = request.form.get('price')
        descreption = request.form.get('descreption')
        stock = request.form.get('stock')

        try:
            good = Good(title=title,price=price,descreption=descreption,stock=int(stock))
            db.session.add(good)
            db.session.commit()
            return {"code":20001,"msg":"添加成功"}
        except Exception as e:
            db.session.rollback()
            raise e
            return {"code":40001,"msg":"添加失败"}
    return render_template('good_add_form.html')
