#coding=utf-8
# 微信聊天+天气预报机器人

# 和风天气https://dev.heweather.com/docs/legacy/api/s6
# 
import requests
import json


def weather_forecast():
    city=input('请输入想要查询的城市名称，如‘江门’:')
    api='https://free-api.heweather.com/s6/weather/'
    weather_type='forecast'
    value={
        'location':city,
        'key':'63d7ffe16c3743e1af28b8ad4423e5af'
}
    
    
    url=api+weather_type
    weather_dict=requests.get(url,params=value).json()
    return weather_dict

def get_data():
    weather_dict=weather_forecast()
    he_weather=weather_dict['HeWeather6']#['daily_forecast']#天气预报，list
    cityname=he_weather[0]['basic']['location']
    daily_forecast=he_weather[0]['basic']
    for i in range(len(daily_forecast)):
        date=daily_forecast[i]['date']
        cond_txt_d=daily_forecast[i]['cond_txt_d']
        cond_txt_n=daily_forecast[i]['cond_txt_n']
        tmp_max=daily_forecast[i]['tmp_max']
        tmp_min=daily_forecast[i]['tmp_min']
        wind_dir=daily_forecast[i]['wind_dir']
        weather_data=cityname+'  '+date+'  白天天气:'+cond_txt_d+'  晚上天气:'+cond_txt_n+'\n最高温:'+ tmp_max +'  最低温:'+tmp_min+'  风向:'+wind_dir
        print(weather_data)




    return True




        



if __name__=="__main__":
        # date=time.strftime('%Y-%m-%d',time.localtime())
        # jinshanApi='http://open.iciba.com/dsapi?date='+date
        # # print(jinshanApi)
        # sentence=get_sentence(jinshanApi)
        # sentenceDict=json.loads(sentence)
        # content=sentenceDict['content']
        # note=sentenceDict['note']

    weather_forecast=get_data()
        # print(type(weather_forecast))
    print(weather_forecast)


