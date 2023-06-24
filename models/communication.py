from models import db
from datetime import datetime

class VisitRecord(db.Model):
    __tablename__ = "visitrecord"
    id = db.Column(db.BigInteger,primary_key=True)
    time = db.Column(db.DateTime,default=datetime.now(),comment="访问时间")
    to = db.Column(comment='访问对象',db.String(32),index=True)
    user = db.Column(comment='来访者',db.String(32),index=True)
    def __repr__(self):
        return self.id

class Like(db.Model):
    __tablename__ = "like"
    id = db.Column(db.BigInteger,primary_key=True)
    to = db.Column(comment='给谁点赞',db.String(32),index=True)
    user = db.Column(comment='谁给我点赞',db.String(32))
    def __repr__(self):
        return self.id

class Favorite(db.Model):
    __tablename__ = "favorite"
    id = db.Column(db.BigInteger,primary_key=True)
    to = db.Column(comment='关注了谁',db.String(32),index=True)
    user = db.Column(comment="谁关注我",db.String(32),index=True)
    def __repr__(self):
        return self.id

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.BigInteger,primary_key=True)
    to = db.Column(comment='给谁评论',db.String(32))
    user = db.Column(comment='谁给我评论',db.String(32))
    content = db.Column(comment='评论内容',db.String(255))
    def __repr__(self):
        return self.id

class Chat(db.Model):
    __tablename__ = "chat"
    id = db.Column(db.BigInteger,primary_key=True)
    to = db.Column(comment='回复消息者',db.String(32))
    user = db.Column(comment='发送消息者',db.String(32))
    chatmsgs = db.relationship('ChatMsg',backref='chat',lazy='select')
    def __repr__(self):
        return self.id


class ChatMsg(db.Model):
    __tablename__ = 'chatmsg'
    id = db.Column(db.BigInteger,primary_key=True)
    to_msg = db.Column(comment='发送者内容',db.String(255))
    reply = db.Column(comment='回复内容',db.String(255))
    chat_id = db.Column(db.BigInteger,db.ForeignKey('chat.id'))
    def __repr__(self):
        return self.id









