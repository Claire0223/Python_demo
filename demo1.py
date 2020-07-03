#coding=utf-8
# 微信聊天+天气预报机器人
# 三个接口
# 金山词霸每日一句：http://open.iciba.com/dsapi/?date=2013-05-03
# 聚合天气：
# 图灵机器人:
import requests
import re
import time
import json

def get_sentence(api):
    sentence=requests.post(api)
    #sentence.encoding=sentence.apparent_encoding
    
    return sentence.text

if __name__=="__main__":
    date=time.strftime('%Y-%m-%d',time.localtime())
    jinshanApi='http://open.iciba.com/dsapi?date='+date
    # print(jinshanApi)
    sentence=get_sentence(jinshanApi)
    sentenceDict=json.loads(sentence)

    content=sentenceDict['content']
    note=sentenceDict['note']


    print ('%s\n%s'%(content,note))

