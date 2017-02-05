from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect

from .forms import ImageUploadForm

from face_client import FaceClient


def introduction(request):
    return render(request, 'software/intro.html', {})


def mypocket(request):
    return render(request, 'software/mypocket.html', {})


def catchsenior(request):
    return render(request, 'software/catchsenior.html', {})


def recognize(request):
    if request.method == 'POST':
        client = FaceClient('f2f4e3c754f940598fe1d5c3cfd8f626', '04632fe53d33463cb8dabeb0ccc6df64')
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #result = client.faces_recognize("esmond", form.cleaned_data['image'], namespace='senior')
            #return render(request, 'software/recognize.html', {'result': result})
            return HttpResponse(form.cleaned_data['image'])

            #return HttpResponseForbidden("form is invalid")
    else:
        return HttpResponseForbidden("allowed via POST")

def rank(request):
    return render(request, 'software/rank.html', {})