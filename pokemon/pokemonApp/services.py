import requests
from weather.services import get_weather


def get_pokemon(api_pokemon):
    response = get_api(api_pokemon)
    return response


def get_types_pokemon():
    normal = get_api('https://pokeapi.co/api/v2/type/1')
    types = get_types_weather()
    count = 0
    pokemon = []
    while count < len(types['pokemon']):
        pokemon.append(types['pokemon'][count]['pokemon'])
        count = count + 1
    count = 0
    while count < len(normal['pokemon']):
        pokemon.append(normal['pokemon'][count]['pokemon'])
        count = count + 1
    return pokemon


def get_types_weather():
    temp_c = get_weather()['temp_c']
    if temp_c > 30:
        types = get_api('https://pokeapi.co/api/v2/type/10')
    else:
        types = get_api('https://pokeapi.co/api/v2/type/1')
    return types


def get_api(api):
    response = requests.get(api)
    return response.json()

