from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect

from .forms import ImageUploadForm
from .models import Senior

from face_client import FaceClient


def introduction(request):
    return render(request, 'software/intro.html', {})


def mypocket(request):

    senior_list = Senior.objects.all()

    return render(request, 'software/mypocket.html', {'senior_list' : senior_list})



def catchsenior(request):
    return render(request, 'software/catchsenior.html', {})


def recognize(request):

    client = FaceClient('167bb22f8cd64970b6360b939fbba1fa', 'd367eb0cdbe94b02b1f68454607de387')
    form = request.GET
    result = client.faces_recognize('all', form['image_url'], namespace='senior')
    name = result['photos'][0]['tags'][0]['uids'][0]['uid']
    image_url = result['photos'][0]['url']
    confidence = result['photos'][0]['tags'][0]['uids'][0]['confidence']

    if confidence > 60:
        s = Senior.objects.create(
            name = name,
            image = image_url
        ).save()

    return render(request, 'software/recognize.html', {'name' : name,
                                                       'image_url' : image_url,
                                                       'confidence' : confidence
                                                       })


def training(request):
    return render(request, 'software/training.html', {})


def training_result(request):

    client = FaceClient('167bb22f8cd64970b6360b939fbba1fa', 'd367eb0cdbe94b02b1f68454607de387')
    form = request.GET
    response = client.faces_detect(form['image_url'])
    tid = response['photos'][0]['tags'][0]['tid']
    client.tags_save(tids=tid, uid=form['name']+'@senior', label=form['name'])
    result = client.faces_train(form['name']+'@senior')

    return render(request, 'software/training_result.html', {'result' : result})


def rank(request):
    return render(request, 'software/rank.html', {})