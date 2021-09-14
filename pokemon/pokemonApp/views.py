from django.shortcuts import render
from pokemonApp.services import get_pokemon


def show_pokemon(request, name):
    pokemon = get_pokemon('https://pokeapi.co/api/v2/pokemon/' + name + '/')
    dictionary = {'pokemon': pokemon}
    return render(request, 'show_pokemon.html', dictionary)

