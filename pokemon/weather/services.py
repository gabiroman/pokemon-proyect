import requests


def get_weather():
    weather = get_api('http://api.weatherapi.com/v1/current.json?key=b89ab893e16346a9a1d132253211009&q=auto:ip&lang=es')
    location = weather['location']['name']
    temp_c = weather['current']['temp_c']
    condition = weather['current']['condition']['text']
    return {'location': location, 'temp_c': temp_c, 'condition': condition}


def get_api(api):
    response = requests.get(api)
    return response.json()