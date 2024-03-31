import httplib2
import json

def Weather():
    url = "https://api.openweathermap.org/data/2.5/forecast?q=bandung,id&appid=27edaa711aa55803ce95bab5bdaa2129"
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    weatherinfo = result
    population = weatherinfo["city"]["population"]
    coord = weatherinfo["city"]["coord"]
    weather = weatherinfo["list"][00]["weather"][0]["description"]
    WeathInf = {"Weather": weather, "Population": population, "Coord": coord}
    weather_list = []
    for i in range(len(weatherinfo["list"])):
        weather_list.append(weatherinfo["list"][i]["weather"][0]["description"])
    weather_list_unq = list(set(weather_list))
    modus_weather = 0
    for j in range(len(weather_list_unq)):
        count = 0
        for k in range(len(weather_list)):
            if weather_list_unq[j] == weather_list[k]:
                count += 1
        if count > modus_weather:
            modus_weather = count
            weather = weather_list_unq[j]
    print("Content-Type: application/json")
    print()
    print(json.dumps(WeathInf, indent=4))
    return

Weather()