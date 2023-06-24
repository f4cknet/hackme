import requests,time

base_url = "https://portal-sit.zhejiangzhongjian.com"
endpoint = "/api/mall-api/app/email/verifyEmailCode"
headers = {"Authorization": "Bearer 85323be9-4b35-4b57-b918-99c15c289f3e"}
data = {"email":"zmzsg100@qq.com"}
for i in range(1,100):
    req = requests.post(base_url+endpoint,json=data,headers=headers)
    print(req.text)
    time.sleep(61)