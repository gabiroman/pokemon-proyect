import requests
from weather.services import get_weather


list_pokemon = []


def get_pokemon(api_pokemon):
    response = get_api(api_pokemon)
    return response


def get_types_pokemon():
    normal = get_api('https://pokeapi.co/api/v2/type/1')
    types = get_type_by_temp()
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


def get_type_by_temp():
    temp_c = get_weather()['temp_c']
    types = get_types()
    type_by_temp = []
    if temp_c >= 26:
        type = get_api('https://pokeapi.co/api/v2/type/' + str(types[9]))
    elif temp_c <= 10:
        type = get_api('https://pokeapi.co/api/v2/type/' + str(types[14]))
    elif temp_c > 10 or temp_c < 26:
        type = get_api('https://pokeapi.co/api/v2/type/' + str(types[10]))
    return type
        

def get_types():
    count = 1
    list_types = []
    while count <= 18:
        name_type = get_api('https://pokeapi.co/api/v2/type/' + str(count))
        list_types.append(name_type['name'])
        count = count + 1
    return list_types


def get_api(api):
    response = requests.get(api)
    return response.json()