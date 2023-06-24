from models import db

class Aituijian(db.Model):
    __tablename__ = "tuijian"
    id = db.Column(db.Integer,primary_key=True)
    host_team = db.Column(db.String(64))
    guest_team = db.Column(db.String(64))
    time = db.Column(db.String(32),comment="开始时间")
    result = db.Column(db.Boolean(0),comment="预测结果")
    def __repr__(self):
        return self.id