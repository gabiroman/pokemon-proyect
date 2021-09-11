import requests
from django.shortcuts import render


def home(request):
    weather = get_weather()
    pokemon = get_pokemon()
    dictionary = {'weather': weather, 'pokemon': pokemon}
    return render(request, 'index.html', dictionary)


def get_weather():
    weather = get_api('http://api.weatherapi.com/v1/current.json?key=b89ab893e16346a9a1d132253211009&q=auto:ip&lang=es')
    location = weather['location']['name']
    temp_c = weather['current']['temp_c']
    condition = weather['current']['condition']['text']
    return {'location': location, 'temp_c': temp_c, 'condition': condition}


def get_pokemon():
    pokemon = get_api('https://pokeapi.co/api/v2/type/10')
    count = 0
    list = []
    while count < len(pokemon['pokemon']):
        list.append(pokemon['pokemon'][count]['pokemon']['name'])
        count = count + 1
    return list


def get_api(api):
    response = requests.get(api)
    return response.json()


# response_pokemon = requests.get(
#    'https://pokeapi.co/api/v2/type/10')
# pokemon = response_pokemon.json()
# count = 0
# while count < len(pokemon['pokemon']):
#    print(pokemon['pokemon'][count]['pokemon']['name'])
#    count = count + 1
