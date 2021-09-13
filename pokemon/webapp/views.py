import requests
from django.shortcuts import render
from weather.services import get_weather
from pokemonApp.services import get_types_pokemon

import random

def home(request):
    weather = get_weather()
    pokemon_by_type = get_types_pokemon()
    pokemon = random.sample(pokemon_by_type, 10)
    dictionary = {'weather': weather, 'pokemon': pokemon}
    return render(request, 'index.html', dictionary)


#print(get_types_pokemon())

# response_pokemon = requests.get(
#    'https://pokeapi.co/api/v2/type/10')
# pokemon = response_pokemon.json()
# count = 0
# while count < len(pokemon['pokemon']):
#    print(pokemon['pokemon'][count]['pokemon']['name'])
#    count = count + 1
