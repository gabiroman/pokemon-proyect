from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import SignUpForm

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/login.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')



def login(request):
    return render(request, 'login/login.html')
