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

# def get_sentence(api):
#     sentence=requests.post(api)
#     #sentence.encoding=sentence.apparent_encoding
    
#     return sentence.text

def get_weatherForecast():
    city=input('请输入想要查询的城市名称，如‘江门’:')
    api='https://free-api.heweather.com/s6/weather/'
    weather_type='forecast'
    value={
        'location':city,
        'key':'63d7ffe16c3743e1af28b8ad4423e5af'
}
    
    url=api+weather_type
    
    #str,需要转为dict
    weatherStr=requests.get(url,params=value).text 
    get_weatherForecase=json.loads(weatherStr)
    

    return get_weatherForecase


        



if __name__=="__main__":
    # date=time.strftime('%Y-%m-%d',time.localtime())
    # jinshanApi='http://open.iciba.com/dsapi?date='+date
    # # print(jinshanApi)
    # sentence=get_sentence(jinshanApi)
    # sentenceDict=json.loads(sentence)
    # content=sentenceDict['content']
    # note=sentenceDict['note']

    weather_forecast=get_weatherForecast()
    # weather_info=weather_forecast['result']
    print(weather_forecast)

    #获得error_code
    # error_code=weather_info['error_code']
    # if error_code==0:
    #     #获取天气信息列表
    #     weather_todaydata=weather_info['today']
    #     today_week=weather_todaydata['week']
    #     today_date=weather_todaydata['date_y']
    #     today_wind=weather_todaydata['wind']
    #     today_temp=weather_todaydata['temperature']
    #     today_weather=weather_todaydata['weather']

    #     print('今天:%s %s\n温度:%s\n%s\n%s\n\n'%(today_week,today_date,today_temp,today_wind,today_weather))

    #     # weather_futuredata=weather_info['future']
    #     # #未来的天气
    #     # print('未来一周的天气：')
    #     # for future_data in weather_futuredata:
    #     #     week=future_data['week']
    #     #     date=future_data['date']
    #     #     temp=future_data['temperature']
    #     #     wind=future_data['wind']
    #     #     print('%s  %s  %s  %s\n'%(week,date,temp,wind))


    # # print ('%s\n%s'%(content,note))
    # # print(type(weather_forecast))
    # # print(weather_forecast)

