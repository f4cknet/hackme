import requests
from lxml import etree
from models import db
from models.tuijian import Aituijian

def crawl():
    f = open('../test/results.txt', 'w')
    for page in range(1,412):
        url = f"http://ai.titan007.com/MatchList.aspx?curPage={page}&akind=1&sclassIdList=&ballkind=0&_=1673269514656"
        req= requests.get(url=url)
        html = etree.HTML(req.text)
        divs = html.xpath("//div[@class='match']")
        # time = divs[0].xpath("//div[@class='time']/text()")
        # host_team = divs[0].xpath("//div[@class='hometeam']/text()")
        # guest_team = divs[0].xpath("//div[@class='guestteam']/text()")
        # win = divs[0].xpath("//img[@class='result']")

        # print(time,host_team,guest_team,win)
            # li[0].xpath("//div[@class='hometeam']/text()"))
            # print(li[0].xpath("//div[@class='time']/text()"))

        num = 0
        win_num=0
        win_lianxu = 0
        loss_lianxu=0
        loss_num = 0
        loss_5 = 0
        win_5 = 0
        win_list = []
        lost_list = []
        touzhu1=-200

        for li in divs:
            num+=1
            win = li[0].attrib.get('class')
            if win=='result':
                win_lianxu+=1
                if loss_lianxu>5:
                    loss_5+=1
                f.write("win,"+ str(loss_lianxu)+'\n')
                # tuijian = Aituijian(host_team=host_team,guest_team=guest_team,time=start_time,result=True)
                loss_lianxu=0


            elif win=="infobox":
                loss_lianxu+=1
                if win_lianxu>5:
                    win_5+=1
                f.write("loss," + str(win_lianxu)+'\n')
                win_lianxu=0

        # f.write(">>>>>>>>>>>>>>>>>>>>win5次以上次数: "+str(win_5)+",loss5次以上次数: "+str(loss_5)+'\n')
crawl()