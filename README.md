# hackme

#### 介绍
基于flask的漏洞靶场，当前包含漏洞如下
1、兑换充值码的高并发漏洞（一码多换）
2、登陆暴力破解漏洞
3、CSRF添加管理员账号
4、微信小程序泄漏session_key
5、评论区XSS

#### 软件架构
FLASK+MYSQL


#### 安装教程

1.  source venv/bin/activate
2.  pip3 install -r requirements.txt
3.  设置环境变量
```log
export SQLUSER="数据库账号"
export SQLPASS="数据库密码"
export wxappid="小程序ID"
export wxsecret="小程序secret"
```
4. source ~/.zshrc 使环境变量生效
5. venv/bin/gunicorn -c gconfig.py -w4 -b0.0.0.0:5000 app:app


#### 参与贡献

#### DEMO
https://api.itner.net