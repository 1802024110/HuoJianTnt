import os
import sys
import json
import login 
import getWebStatu
import WeCom_nodream
baseUrl = getWebStatu.getWebUrl()
checkUrl = baseUrl + 'user/checkin'
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
# 初始化企业微信参数
CORPID = os.environ['CORPID'] 
CORPSECRET = os.environ['CORPSECRET']
# 应用的ID
if __name__ == "__main__":
  loginCode =  login.login(username, password)
  if loginCode != 1: 
    print('登录失败')
  session = login.session
  # 请求签到
  checkin = session.post(checkUrl).text
  checkin = json.loads(checkin)
  # 签到状态
  if checkin['ret'] == 1:
    AGENTID1 = os.environ['AGENTID1'] 
    print(AGENTID1, CORPID, CORPSECRET)
    wecom = WeCom_nodream.WeCom(AGENTID1, CORPID, CORPSECRET)
    wecom.sendCardMsg("火箭TNT签到成功",str(checkin['msg']),'https://github.com/1802024110/HuoJianTnt','火箭TNT')
  else:
    AGENTID2 = os.environ['AGENTID2'] 
    print(AGENTID2, CORPID, CORPSECRET)
    wecom = WeCom_nodream.WeCom(AGENTID2, CORPID, CORPSECRET)
    wecom.sendCardMsg("火箭TNT签到失败",str(checkin['msg']),'https://github.com/1802024110/HuoJianTnt','火箭TNT')