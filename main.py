import sys
import json
import login 
import getWebStatu
baseUrl = getWebStatu.getWebUrl()
checkUrl = baseUrl + 'user/checkin'
username = sys.argv[1]
password = sys.argv[2]
corpid = sys.argv[3]
# 企业ID
corpsecret = sys.argv[4]
# 应用的凭证密钥
agentid = sys.argv[5]
# 应用的ID
""" corpid='wwb330a036235c91ea'
corpsecret='bpKk0puHo__K2WM2C4SDxZFRDOfxgFJnvW_vQy6HmhA'
agentid='1000002'
username, password = '1802024110@qq.com', '2002zengyuan' """
if __name__ == "__main__":
  print("用户名：" + username)
  print("密码：" + password)
  print("企业ID：" + corpid)
  print("应用的凭证密钥：" + corpsecret)
  print("应用的ID：" + agentid)
  loginCode =  login.login(username, password)
  if loginCode != 1: 
    print('登录失败')
  session = login.session
  # 请求签到
  checkin = session.post(checkUrl).text
  checkin = json.loads(checkin)
  if corpid != '':
    # 签到状态
    if checkin['ret'] == 1:
      session.get(f'https://api.htm.fun/api/Wechat/text/?corpid={corpid}&corpsecret={corpsecret}&agentid={agentid}&text=火箭TNT签到成功')
    else:
      msg = checkin['msg']
      session.get(f'https://api.htm.fun/api/Wechat/text/?corpid={corpid}&corpsecret={corpsecret}&agentid={agentid}&text=火箭TNT签到失败，原因：{msg}')