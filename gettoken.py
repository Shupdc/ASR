
# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=mmAQp5nplLB5p8j8urY1ahZe&client_secret=hxGaYCh05rjkwfw7ydgaiI11tC7h7Kgh'
response = requests.get(host)
if response:
    print(response.json())
