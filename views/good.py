# from models import db
# from lib.good import Good
# from flask import Blueprint,request,render_template
#
# good_blue = Blueprint('good',__name__,url_prefix='/good')
#
# @good_blue.route('/list',methods=['GET'])
# def goodlist():
#     data = Good.query.all()
#     return render_template('good_list.html',data=data)
#
# @good_blue.route('/detail',methods=["GET"])
# def gooddetail():
#     good_id = request.args.get('id')
#     result = db.session.query(Good).filter_by(id=good_id).first()
#     return render_template('good_detail.html',data=result)