from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ImageUploadForm

from .models import Catching
from .models import Senior
from .models import Chatting
from .models import User

from face_client import FaceClient


def introduction(request):
    return render(request, 'software/intro.html', {})


@login_required
def mypocket(request):

    form = request.POST

    senior = Senior.objects.get(student_id=form['student_id'])
    catching = Catching.objects.filter(senior=senior).update(comment=form['comment'])

    catching_list = Catching.objects.all()

    return render(request, 'software/mypocket.html', {'catching_list' : catching_list})


@login_required
def chatting(request):
    form = request.POST

    chatting = Chatting.objects.create(
  #      name=form['name'],
        chat=form['chat'],
        senior = Senior.objects.get(pk=form['senior'])
        )

    senior = get_object_or_404(Senior, pk=chatting.senior.pk)
    catching_list = Catching.objects.filter(senior=chatting.senior)
    chatting_list = Chatting.objects.filter(senior=chatting.senior)
    return render(request, 'software/senior.html', {'senior': senior, 'catching_list' : catching_list, 'chatting_list': chatting_list})


@login_required
def catchsenior(request):
    return render(request, 'software/catchsenior.html', {})


@login_required
def recognize(request):

    client = FaceClient('167bb22f8cd64970b6360b939fbba1fa', 'd367eb0cdbe94b02b1f68454607de387')
    form = request.GET
    result = client.faces_recognize('all', form['image_url'], namespace='senior2')
    student_id = result['photos'][0]['tags'][0]['uids'][0]['uid'].split('@')[0]
    senior = Senior.objects.filter(student_id=student_id).first()
    name = senior.name
    image_url = result['photos'][0]['url']
    confidence = result['photos'][0]['tags'][0]['uids'][0]['confidence']

    s = Catching.objects.create(
        image = form['image_url'],
        senior = senior,
        user = User.objects.first()
    )

    if form.get('confidence', False) > 60:
        s.update(is_succeed=True)


    return render(request, 'software/recognize.html', {'name' : name,
                                                       'image_url' : image_url,
                                                       'confidence' : confidence,
                                                       'student_id' : student_id
                                                       })

@login_required
def senior(request, pk):
    senior = get_object_or_404(Senior, pk=pk)
    catching_list = Catching.objects.filter(senior=Senior.objects.get(pk=pk))
    chatting_list = Chatting.objects.filter(senior=Senior.objects.get(pk=pk))
    return render(request, 'software/senior.html', {'senior': senior, 'catching_list' : catching_list, 'chatting_list': chatting_list})


@login_required
def seniors(request):
    seniors = Senior.objects.all()
    return render(request, 'software/seniors.html', {'seniors' : seniors})


@login_required
def seniors_search(request):
    result = request.GET['searched_name']
    seniors = Senior.objects.filter(name=result)
    return render(request, 'software/seniors.html', {'seniors': seniors})


@login_required
def training(request):
    return render(request, 'software/training.html', {})


@login_required
def training_result(request):
        form = request.GET

    if not Senior.objects.filter(student_id=form['student_id']):
        Senior.objects.create(
            name = form['name'],
            image = form['image_url'],
            student_id = form['student_id']
            )

    client = FaceClient('ddc12042e3c940f3a0d1a4d264da9447', 'fd724e4460c848e3ae784faaf5342904')
    response = client.faces_detect(form['image_url'])
    tid = response['photos'][0]['tags'][0]['tid']
    client.tags_save(tids=tid, uid=form['student_id']+'@senior2', label=form['student_id'])
    result = client.faces_train(form['student_id']+'@senior2')

    return render(request, 'software/training_result.html', {'result' : result})


@login_required
def rank(request):
    return render(request, 'software/rank.html', {})