from flask import Flask,request,session,make_response,render_template,jsonify
import requests,json
from flask_migrate import Migrate
from lib.decryptweixin import decrypt
from models import db,redis_client
import config
from views import admin,user,weixin,qiutan_tuijian
import logging
from flask_cors import CORS


logging.basicConfig(filename='./log/myapp.log',level=logging.DEBUG)


app = Flask(__name__)
app.config.from_object("config.DevConfig")
db.init_app(app)
redis_client.init_app(app)
# CORS(app, resources={r"/*": {"origins": "*"}})
# with app.app_context():
#     db.drop_all()
#     db.create_all()
app.register_blueprint(admin.admin_blue)
app.register_blueprint(user.user_blue)
app.register_blueprint(weixin.weixin_blue)
app.register_blueprint(qiutan_tuijian.qiutan_blue)
migrate = Migrate(app,db)

APP_ID = config.weixin.get('appid')
APP_SECRET = config.weixin.get('secret')
app.secret_key = 'sdertyuhgfd23456q'


@app.route('/getuserinfo',methods=["POST"])
def getuserinfo():
    data = request.json
    code = data.get('code')
    encryptdata = data.get('encryptedData')
    iv = data.get('iv')
    session_url = f"https://api.weixin.qq.com/sns/jscode2session?appid={APP_ID}&secret={APP_SECRET}&grant_type=authorization_code&js_code="+code
    info = requests.get(session_url,verify=False)
    session_key_openID = json.loads(info.text)
    result = decrypt(APP_ID,session_key_openID.get('session_key'),encryptdata,iv)
    print(result)
    return result


@app.route('/feedback',methods=['POST','GET'])
def feedback():
    if request.method == "POST":
        email = request.form.get('email')
        feedback = request.form.get('feedback')
        try:
            feed = Feedback(email=email,feedback=feedback)
            db.session.add(feed)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    try:
        result = Feedback.query.all()
    except Exception as e:
        raise e

    return render_template('feedback.html',data=result)

@app.route('/log',methods=['GET'])
def log():
    with open("./log/myapp.log",'r')as f:
        result = f.readlines()
    return result

@app.route('/circle',methods=["GET"])
def circle():
    return {"code":20001,"data":"asd"}

@app.route('/notice',methods=["GET"])
def notice():
    return {"code":20001,"data":"防诈提示"}


@app.route('/',methods=['GET'])
def index():
    return "12345"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)

