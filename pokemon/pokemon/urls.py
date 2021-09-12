from django.contrib import admin
from django.urls import path
from webapp.views import home
from pokemonApp.views import show_pokemon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('pokemon/<str:name>', show_pokemon)
]
