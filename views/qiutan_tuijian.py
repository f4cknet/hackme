from flask import Blueprint,request
from models.tuijian import Aituijian
from lib.ai_titan007 import crawl

qiutan_blue = Blueprint('qiutan',__name__,url_prefix='/qiutan')

@qiutan_blue.route('/crawl_qiutanai',methods=['GET'])
def start_crawl():
    return "crawl"