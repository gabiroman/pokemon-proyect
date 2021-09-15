import requests
import random
from weather.services import get_weather


def get_pokemon_home():
    pokemon = get_name_pokemon()
    list_pokemon = []
    for p in pokemon:
        list_pokemon.append(get_pokemon(
            'https://pokeapi.co/api/v2/pokemon/' + p + '/'))
    return list_pokemon


def get_pokemon(api_pokemon):
    response = get_api(api_pokemon)
    return response


def get_name_pokemon():
    types = get_type_by_temp()
    pokemon = []
    for t in types:
        pokemon.extend(iteration_name(get_api('https://pokeapi.co/api/v2/type/' + str(t))))
    return random.sample(pokemon, 10)


def get_type_by_temp():
    temp_c = get_weather()['temp_c']
    types = [1]
    if temp_c >= 26:
        types.append(10)
    elif temp_c <= 10:
        types.append(15)
    elif temp_c > 10 or temp_c < 26:
        types.append(12)
    return types


def iteration_name(json):
    count = 0
    list_pokemon = []
    while count < len(json['pokemon']):
        list_pokemon.append(json['pokemon'][count]['pokemon']['name'])
        count = count + 1
    return random.sample(list_pokemon, 10)


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
