import requests 

url = "https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=58d6040c-dca7-407f-a244-d0bfdfa8144a&limit=1000&sort=ImportDate%20desc&format=JSON"
data = requests.get(url , verify = False)
json = data.json()
for i in json['records']:
    print(i["county"] + " " + i["sitename"],end = "，")
    print("AQI : " + i["aqi"] , end = "，")
    print("空氣品質" + i["status"])
