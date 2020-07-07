#和风天气接口
import requests
import json

url='https://free-api.heweather.com/s6/weather/'
weatherType='forecast'#天气类型:now实况   forecast3-10天预报   hourly逐小时预报    lifetype生活指数
# key='63d7ffe16c3743e1af28b8ad4423e5af'
city=input('输入城市名称:\n')
value={
    'location':city,
    'key':'63d7ffe16c3743e1af28b8ad4423e5af'
}
apiurl=url+weatherType
rs=requests.get(apiurl,params=value).text
weatherDict=json.loads(rs)

#获取日期date、实时天气概况re(cond_txt.*?)、温度。
print(weatherDict)







# if __name__=='__main__':
#     print(get_weather())


