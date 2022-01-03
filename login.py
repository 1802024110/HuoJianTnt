import requests
import json
import getWebStatu
# 获得可用的网页
baseUrl = getWebStatu.getWebUrl()
# 拼接登录的URL
loginUrl = baseUrl + 'auth/login'
# 一个session对象，可以持久化保存cookies
session = requests.session()
def login(usernaem,password):
  # data数据
  data = {
  'email': usernaem,
  'passwd': password,
  'code': ''
}
  # 发送post请求
  response = session.post(loginUrl,data=data).text
  requests = json.loads(response)
  ret = requests['ret']
  # 如果登录成功，则返回1
  return ret