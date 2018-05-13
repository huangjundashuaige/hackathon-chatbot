  # coding=utf-8
import urllib,urllib.request
import json
import time
import hashlib
import urllib.parse
import requests


class YouDaoFanyi:
    def __init__(self, appKey, appSecret):
        self.url = 'https://openapi.youdao.com/api/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        }
        self.appKey = appKey  # 应用id
        self.appSecret = appSecret  # 应用密钥
        self.langFrom = 'auto'   # 翻译前文字语言,auto为自动检查
        self.langTo = 'EN'     # 翻译后文字语言,auto为自动检查

    def getUrlEncodedData(self, queryText):
        '''
        将数据url编码
        :param queryText: 待翻译的文字
        :return: 返回url编码过的数据
        '''
        salt = '2'  # 产生随机数 ,其实固定值也可以,不如"2"
        sign_str = self.appKey + queryText + salt + self.appSecret
        sign_str=sign_str.encode('utf-8')
        sign = hashlib.md5(sign_str).hexdigest()
        payload = {
            'q': queryText,
            'from': self.langFrom,
            'to': self.langTo,
            'appKey': self.appKey,
            'salt': salt,
            'sign': sign
        }

        # 注意是get请求，不是请求
        data = urllib.parse.urlencode(payload)
        return data

    def parseHtml(self, html):
        '''
        解析页面，输出翻译结果
        :param html: 翻译返回的页面内容
        :return: None
        '''
        data = json.loads(html)

        print ('-------------------------') 
        #print(data)
        translationResult = data['translation']
        if isinstance(translationResult, list):
            translationResult = translationResult[0]
        print (translationResult)
        return translationResult
        if "basic" in data:
            youdaoResult = "\n".join(data['basic']['explains'])
            print ('有道词典结果--')
            print (youdaoResult)
            
        print ('-------------------------')

    def translate(self, queryText):
        data = self.getUrlEncodedData(queryText)  # 获取url编码过的数据
        target_url = self.url + '?' + data    # 构造目标url
        print('目标url：'+target_url)
        # request = urllib2.Request(target_url, headers=self.headers)  # 构造请求
        req = requests.get(target_url, headers=self.headers)  # 构造请求
        # with request.urlopen(request) as response111: # 发送请求
        req.encoding='utf-8'
        html=req.text
        return self.parseHtml(html)    # 解析，显示翻译结果


def fanyi(input):
    print('程序开始运行！')
    appKey = '2f95c2bf54998831'  # 应用id
    appSecret = 'JbX7X5oo5jLXbh2L4yBsyykWndma2g55'  # 应用密钥
    fanyi = YouDaoFanyi(appKey, appSecret)
    queryText = input.strip()
    return fanyi.translate(queryText)