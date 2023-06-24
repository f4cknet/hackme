from models import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.String(32),primary_key=True)
    phone = db.Column('phone', db.String(11), nullable=True)
    openId = db.Column('openId',db.String(128),unique=True)
    userdetail = db.relationship('UserDetail',backref='user',uselist=False,lazy='select')
    create_time = db.Column(db.DateTime,default=datetime.now())
    educations_verify = db.Column(db.Boolean(0),default=False,comment="教育认证")
    occupation_verify = db.Column(db.Boolean(0),default=False,comment="工作认证")
    idcard_verify = db.Column(db.Boolean(0),default=False,comment="实名认证")
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))
    status = db.Column(db.Boolean(0),comment="是否上架")
    login_time = db.Column(db.Integer,index=True,comment="登陆次数") # 活跃度
    score = db.Column(db.Integer,index=True,comment="推荐分")
    like_favorite = db.Column(db.Integer,index=True,comment="收藏+点赞")
    loginrecords = db.relationship('LoginRecord',backref='user',lazy='dynamic')


    def __repr__(self):
        return self.id

class UserDetail(db.Model):
    __tablename__ = "userdetail"
    id = db.Column(db.Integer,primary_key=True)
    wechat = db.Column(db.String(16),unique=True)
    nickname = db.Column(db.String(32))
    sex = db.Column(db.Enum('男', '女'), nullable=False)
    height = db.Column(db.String(3))
    income = db.Column(db.Enum('0w-10w','10w-20w','20w-30w','30w-40w','40w-50w','50w以上'))
    expect_marry = db.Column(db.Enum('0-1年','1-2年','2-3年','3-4年','4年以上'))
    content = db.Column(db.Text())
    expect = db.Column(db.Text())
    real_name = db.Column(db.String(16))
    idcard = db.Column(db.String(32))
    address = db.Column(db.Integer,db.ForeignKey('useraddress.id'))
    car_id = db.Column(db.Integer,db.ForeignKey('car.id'))
    education_id = db.Column(db.Integer,db.ForeignKey('education.id'))
    occupation_id = db.Column(db.Integer,db.ForeignKey('occupation.id'))
    user_id = db.Column(db.String(32),db.ForeignKey('user.id'))
    house_id = db.Column(db.Integer,db.ForeignKey('house.id'))
    media = db.relationship('Media',backref='userdetail',lazy='dynamic')
    def __repr__(self):
        return self.id

class UserAddress(db.Model):
    __tablename__ = "useraddress"
    id = db.Column(db.Integer, primary_key=True)
    userdetail = db.relationship('UserDetail',backref='useraddress',lazy='select')
    provice = db.Column(db.String(16),nullable=False)
    city = db.Column(db.String(16),nullable=False)
    district = db.Column(db.String(16),nullable=False)
    detail = db.Column(db.String(256),nullable=False)
    def __repr__(self):
        return self.id

class Media(db.Model):
    __tablename__ = "media"
    id = db.Column(db.Integer,primary_key=True)
    media_url = db.Column(db.String(256))
    categories = db.Column(db.Enum('1','2')) #1照片 ，2视频
    userdetail_id = db.Column(db.Integer,db.ForeignKey('userdetail.id'))
    def __repr__(self):
        return self.id


class Education(db.Model):
    __tablename__ = "education"
    id = db.Column(db.Integer,primary_key=True)
    school = db.Column(db.String(64))
    level = db.Column(db.Enum('初中', '高中', '大专', '本科', '硕士', '博士'))
    userdetail = db.relationship('UserDetail',backref='education',lazy="select")
    def __repr__(self):
        return self.id

class Car(db.Model):
    __tablename__ = "car"
    id = db.Column(db.Integer,primary_key=True)
    license = db.Column(db.String(255))
    userdetail = db.relationship('UserDetail',backref='car',lazy='select')
    def __repr__(self):
        return self.id

class House(db.Model):
    __tablename__ = "house"
    id = db.Column(db.Integer,primary_key=True)
    license = db.Column(db.String(255))
    userdetail = db.relationship('UserDetail',backref='house',lazy='select')
    def __repr__(self):
        return self.id

class Occupation(db.Model):
    __tablname__ = "occupation"
    id = db.Column(db.Integer,primary_key=True)
    job = db.Column(db.String(16),nullable=False)
    company = db.Column(db.String(64))
    userdetail = db.relationship('UserDetail',backref='occupation',lazy='select')
    def __repr__(self):
        return self.id

class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column('rolename',db.String(16),unique=True)
    users = db.relationship('User',backref='role',lazy='dynamic')


class RechargeCard(db.Model):
    __tablename__ = "rechargecard"
    id = db.Column(db.Integer,primary_key=True)
    code = db.Column('code',db.String(16),unique=True)
    isused = db.Column('isused',db.Boolean(0),default=False)
    user_id = db.Column(db.String(32),db.ForeignKey('user.id'))
    price = db.Column(db.Integer)

    def __repr__(self):
        return self.id

class RechargeRecord(db.Model):
    __tablename__ = "rechargerecord"
    id = db.Column(db.Integer,primary_key=True)
    time = db.Column('充值时间',db.DateTime,default=datetime.now())
    status = db.Column('成功/失败',db.Boolean(0))
    money = db.Column('充值金额',db.Float(10))
    user_id = db.Column(db.String(32),db.ForeignKey('user.id'))
    def __repr__(self):
        return self.id

class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(32))
    feedback = db.Column(db.String(128))

    def __repr__(self):
        return str(self.id)

class LoginRecord(db.Model):
    __tablename__ = "loginrecord"
    id = db.Column(db.BigInteger,primary_key=True)
    time = db.Column(db.DateTime,comment="登陆时间")
    user_id = db.Column(db.String(32),db.ForeignKey('user.id'),index=True)
    def __repr__(self):
        return self.id