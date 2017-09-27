from urllib import request
import json
import city

while True:
    city_name = input()
    city_code = city.city.get(city_name)
    if city_code is None: 
        exit(0)
    url = r"http://www.weather.com.cn/data/cityinfo/" + city_code + r".html"
    response = request.urlopen(url); 
    page = response.read()
    page = page.decode('utf-8')
    print(json.dumps(page))
    page = json.loads(page)
    print(city_name, "天气为:", page.get("weatherinfo").get("weather"),
          "最低气温:", page.get("weatherinfo").get("temp1"), "最高气温:",
          page.get("weatherinfo").get("temp2"))




