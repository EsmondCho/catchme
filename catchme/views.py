from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy


def home(request):
    return render(request, 'software/intro.html', {})


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
