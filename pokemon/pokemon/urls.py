from django.contrib import admin
from django.urls import path, include
from webapp.views import home
from pokemonApp.views import show_pokemon
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('pokemon/<str:name>', show_pokemon),

    #for the facebook allauth
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
