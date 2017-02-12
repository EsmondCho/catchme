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

    client = FaceClient('167bb22f8cd64970b6360b939fbba1fa', 'd367eb0cdbe94b02b1f68454607de387')
    form = request.GET
    result = client.faces_recognize('all', form['image_url'], namespace='senior')
    name = result['photos'][0]['tags'][0]['uids'][0]['uid']
    image_url = result['photos'][0]['url']
    confidence = result['photos'][0]['tags'][0]['uids'][0]['confidence']

    return render(request, 'software/recognize.html', {'result' : result,
                                                       'name' : name,
                                                       'image_url' : image_url,
                                                       'confidence' : confidence
                                                       })



def rank(request):
    return render(request, 'software/rank.html', {})