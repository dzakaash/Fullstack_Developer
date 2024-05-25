import httplib2
import json

def CompanyCountry():
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    car_data = result
    ComCount = []
    print(len(car_data))
    for Re in car_data["Results"]:
        ComCount.append({"Country":Re["Country"], "Company":Re["Mfr_Name"]})
    print(json.dumps(ComCount, indent=4))
    return

CompanyCountry()