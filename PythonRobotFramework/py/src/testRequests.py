import requests

if False:
    # api-endpoint
    URL = "http://dingdata.nl/premie"

    # get request naar api uitvoeren
    r = requests.get(url=URL, params={'geslacht':'man', 'geboortejaar':1970, 'inkomen':45000, 'kinderen':2})

    # response body converteren naar JSON
    response = r.json()

    #print(response)

    # in python de JSON response body als variabelen gebruiken
    print("inkomen", response["resultaten"]["inkomen"])
    print("Leeftijd", response["resultaten"]["leeftijd"])

elif True:
    # api-endpoint
    URL = "http://127.0.0.1:5000/api/onderdelenlijst"

    # POST body klaarmaken en POST versturen
    part_data = {
        "nummer":48,
        "naam":"cranc",
        "omschrijving":"Trapper cranc aluminimum",
        "aantal":12
    }

    # Request uitvoeren
    r = requests.post(url = URL, json = part_data)