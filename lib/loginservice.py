from models import db
from models.user import User
from models.admin import Admin

def verify_user(phone,password):
    result = db.session.query(User).filter_by(phone=phone).first()
    try:
        if result.password == password:
            return  result
        else:
            return False
    except Exception as e:
        print(e)

def verify_admin(username,password):
    result = db.session.query(Admin).filter_by(username=username).first()
    try:
        if result.password == password:
            return result
        else:
            return False
    except Exception as e:
        print(e)