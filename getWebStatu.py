# 初始化Python
import requests
# 网页列表
webList = [
    'https://www.hjtnt.buzz/',
    'https://www.hjtnt.cc/',
    'https://www.hjtnt.com/',
    'https://www.hjtnt.cc/',
    'hhttps://koozk.com/'
]
headers = {
  'authority': 'www.hjtnt.buzz',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
# 测试是否有可用网页
def getWebUrl():
  for web in webList:
    try:
        # 创建一个新的连接
        webCon = requests.request("GET", web, headers=headers,timeout=5)
        # 获取网页的状态码
        code = webCon.status_code
        # 如果状态码为200，则打印网页地址和状态码
        if code == 200:
            return web
    except Exception as e:
        print(e)
        continue
  return None