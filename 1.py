import requests
from util import readConfig

path = '/api3/ec/navigation/page/getPageModule'
# token = ''
#

readConfig = readConfig.ReadConfig()
url = readConfig.get_http('baseurl_prod')
base_url = url + path
print(base_url)


header = {
    'Content-Type':'application/json',
    'X-WX-Token':'jsc2skp.3a4e5566-6580-41c9-9714-cf82770482d5'
}

data = {
    "storeId": 1667042,
    "appid": "wx14e13dda1144f484",
    "env": "production",
    "templateId": 56,
    "pid": "42",
    "wxTemplateId": 56,
    "refer": "",
    "openid": "oY84P5ak0Rq8pDhSTqnGbhVDR9Qg",
    "source": 1,
    "sdpSource": "ec",
    "pageModuleId": 494,
    "pageType": "home"
}

r = requests.post(url=base_url,json=data,headers=header)

# response = requests.request("POST", url, data=data, headers=header)

print(r.text)

