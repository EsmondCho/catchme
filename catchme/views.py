from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from .forms import UserForm, UserProfileForm


def home(request):
    return render(request, 'software/intro.html', {})


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

"""
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() and upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect('/')
    else:
        uf = UserForm()
        upf = UserProfileForm()
    return render(request, 'registration/register.html', { 'userform' : uf, 'userprofileform' : upf})
"""