import requests
from django.shortcuts import render
from weather.services import get_weather
from pokemonApp.services import get_pokemon_home

import random

def home(request):
    weather = get_weather()
    pokemon = get_pokemon_home()
    dictionary = {'weather': weather, 'pokemon': pokemon}
    return render(request, 'index.html', dictionary)
