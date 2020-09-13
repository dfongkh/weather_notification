import requests
#import json
#import pprint

def get_data(data_type, lang='en'):
    api_base_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    endpoint_path = f"?dataType={data_type}&lang={lang}"
    full_api_url = f"{api_base_url}{endpoint_path}"
    r = requests.get(full_api_url)
    #pprint.pprint(r.json())
    if r.status_code in range(200,299):
        return r.json()

"""
dataType
flw: Local Weather Forecast
fnd: 9-day Weather Forecast
rhrread: Current Weather Report
warnsum: Weather Warning Summary
warningInfo: Weather Warning Information
swt: Special Weather Tips

lang
en: English
tc: Traditional Chinese
sc: Simplified Chinese
"""

def current_temp(temp_location):
    data_type = "rhrread"
    data = get_data(data_type)
    return data["temperature"]["data"][temp_location]['value']

#print(f"Current Temperature at Home is {current_temp(24)}°C")

def current_humidity():
    data_type = "rhrread"
    data = get_data(data_type)
    return data["humidity"]["data"][0]['value']

def current_rainfall(rain_location):
    data_type = "rhrread"
    data = get_data(data_type)
    return data["rainfall"]["data"][rain_location]['max'] 




"""
Location Num

temperature

data1 = get_data("rhrread")
for i,j in enumerate(data1["temperature"]["data"]):
    print(i, j["place"])

0 King's Park
1 Hong Kong Observatory
2 Wong Chuk Hang
3 Ta Kwu Ling
4 Lau Fau Shan
5 Tai Po
6 Sha Tin
7 Tuen Mun
8 Tseung Kwan O
9 Sai Kung
10 Chek Lap Kok
11 Tsing Yi
12 Shek Kong
13 Tsuen Wan Ho Koon
14 Tsuen Wan Shing Mun Valley
15 Hong Kong Park
16 Shau Kei Wan
17 Kowloon City
18 Happy Valley
19 Wong Tai Sin
20 Stanley
21 Kwun Tong
22 Sham Shui Po
23 Kai Tak Runway Park
24 Yuen Long Park
25 Tai Mei Tuk



rainfall

0 Central &amp; Western District
1 Eastern District
2 Kwai Tsing
3 Islands District
4 North District
5 Sai Kung
6 Sha Tin
7 Southern District
8 Tai Po
9 Tsuen Wan
10 Tuen Mun
11 Wan Chai
12 Yuen Long
13 Yau Tsim Mong
14 Sham Shui Po
15 Kowloon City
16 Wong Tai Sin
17 Kwun Tong

"""

"""
{   
    "rainfall":
    {"data":
    [
        {"unit":"mm","place":"中西區","max":0,"main":"FALSE"},
        {"unit":"mm","place":"東區","max":0,"main":"FALSE"},
        {"unit":"mm","place":"葵青","max":0,"main":"FALSE"},
        {"unit":"mm","place":"離島區","max":0,"main":"FALSE"},
        {"unit":"mm","place":"北區","max":0,"main":"FALSE"},
        {"unit":"mm","place":"西貢","max":0,"main":"FALSE"},
        {"unit":"mm","place":"沙田","max":0,"main":"FALSE"},
        {"unit":"mm","place":"南區","max":0,"main":"FALSE"},
        {"unit":"mm","place":"大埔","max":0,"main":"FALSE"},
        {"unit":"mm","place":"荃灣","max":0,"main":"FALSE"},
        {"unit":"mm","place":"屯門","max":0,"main":"FALSE"},
        {"unit":"mm","place":"灣仔","max":0,"main":"FALSE"},
        {"unit":"mm","place":"元朗","max":0,"main":"FALSE"},
        {"unit":"mm","place":"油尖旺","max":0,"main":"FALSE"},
        {"unit":"mm","place":"深水埗","max":0,"main":""},
        {"unit":"mm","place":"九龍城","max":0,"main":""},
        {"unit":"mm","place":"黃大仙","max":0,"main":"FALSE"},
        {"unit":"mm","place":"觀塘","max":0,"main":"FALSE"}

        ],
    
    "startTime":"2020-08-29T20:45:00+08:00",
    "endTime":"2020-08-29T21:45:00+08:00"
    },

    "warningMessage":["酷熱天氣警告現正生效，市民應慎防中暑，多補充水分。"],
    "icon":[77],
    "iconUpdateTime":"2020-08-29T18:00:00+08:00",
    "uvindex":"",
    "updateTime":"2020-08-29T22:02:00+08:00",

    "temperature":
    {"data":
    [
        {"place":"京士柏","value":29,"unit":"C"},
        {"place":"香港天文台","value":30,"unit":"C"},
        {"place":"黃竹坑","value":28,"unit":"C"},
        {"place":"打鼓嶺","value":29,"unit":"C"},
        {"place":"流浮山","value":29,"unit":"C"},
        {"place":"大埔","value":29,"unit":"C"},
        {"place":"沙田","value":29,"unit":"C"},
        {"place":"屯門","value":28,"unit":"C"},
        {"place":"將軍澳","value":28,"unit":"C"},
        {"place":"西貢","value":29,"unit":"C"},
        {"place":"赤鱲角","value":31,"unit":"C"},
        {"place":"青衣","value":29,"unit":"C"},
        {"place":"石崗","value":28,"unit":"C"},
        {"place":"荃灣可觀","value":26,"unit":"C"},
        {"place":"荃灣城門谷","value":27,"unit":"C"},
        {"place":"香港公園","value":29,"unit":"C"},
        {"place":"筲箕灣","value":29,"unit":"C"},
        {"place":"九龍城","value":29,"unit":"C"},
        {"place":"跑馬地","value":28,"unit":"C"},
        {"place":"黃大仙","value":29,"unit":"C"},
        {"place":"赤柱","value":29,"unit":"C"},
        {"place":"觀塘","value":30,"unit":"C"},
        {"place":"深水埗","value":29,"unit":"C"},
        {"place":"啟德跑道公園","value":29,"unit":"C"},
        {"place":"元朗公園","value":29,"unit":"C"},
        {"place":"大美督","value":29,"unit":"C"}
        ],

        "recordTime":"2020-08-29T22:00:00+08:00"
        },
        
    "tcmessage":"",
    "mintempFrom00To09":"",
    "rainfallFrom00To12":"",
    "rainfallLastMonth":"",
    "rainfallJanuaryToLastMonth":"",
    "humidity":
    {"recordTime":"2020-08-29T22:00:00+08:00",
    "data":[{"unit":"percent","value":76,"place":"香港天文台"}]
    }
    
}
"""
