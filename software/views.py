from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect

from .forms import ImageUploadForm
from .models import Senior

from face_client import FaceClient


def introduction(request):
    return render(request, 'software/intro.html', {})


def mypocket(request):
    return render(request, 'software/mypocket.html', {})


def catchsenior(request):
    return render(request, 'software/catchsenior.html', {})


def recognize(request):
    if request.method == 'POST':
        f = request.POST
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            s = Senior.objects.create(
                name = f['name'],
                image = form.cleaned_data['image']
            )
            s.save()
            client = FaceClient('f2f4e3c754f940598fe1d5c3cfd8f626', '04632fe53d33463cb8dabeb0ccc6df64')
            image_url = 'http://192.168.1.21:8000' + s.image.url
            #result = client.faces_recognize("esmond", image_url, namespace='senior')
            return render(request, 'software/recognize.html', {'result': image_url})

        return HttpResponseForbidden("form is invalid")
    else:
        return HttpResponseForbidden("allowed via POST")

def rank(request):
    return render(request, 'software/rank.html', {})