from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ImageUploadForm

from .models import *
from face_client import FaceClient


def introduction(request):
    return render(request, 'software/intro.html', {})


@login_required
def mypocket(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = request.POST

        senior = Senior.objects.get(student_id=form['student_id'])
        senior.caught_count += 1
        senior.save()

        profile.catching_count += 1
        profile.save()

        ex_catching = Catching.objects.filter(user=profile).filter(senior=senior).filter(is_in_pocket=True)
        if ex_catching:
            ex_catching[0].is_in_pocket = False

        catching = Catching.objects.create(
            image=form['image_url'],
            is_in_pocket=True,
            confidence=form['confidence'],
            comment=form['comment'],
            senior=senior,
            user=profile
        )
        catching.save()

    catching_count = profile.catching_count
    catching_list = Catching.objects.filter(user=profile).filter(is_in_pocket=True)

    return render(request, 'software/mypocket.html', {'catching_list': catching_list,
                                                      'catching_count': catching_count})


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

    if request.method == 'POST':
        form = request.POST

        client = FaceClient('46675e3d05934138bcb4e9b93880e959', 'a62bca207a57467784f86e37a4241b2a')
        result = client.faces_recognize('all', form['image_url'], namespace='senior')

        student_id = result['photos'][0]['tags'][0]['uids'][0]['uid'].split('@')[0]
        image_url = result['photos'][0]['url']
        confidence = result['photos'][0]['tags'][0]['uids'][0]['confidence']

        senior = Senior.objects.get(student_id=student_id)
        senior_id = senior.id
        senior_name = senior.name

        return render(request, 'software/recognize.html', {'senior_name': senior_name,
                                                           'image_url': image_url,
                                                           'confidence': confidence,
                                                           'student_id': student_id
                                                           })
    else:
        return HttpResponseForbidden('Allowed via POST')



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

    if request.method == 'POST':
        form = request.POST

        if not Senior.objects.filter(student_id=form['student_id']):
            senior = Senior.objects.create(
                name=form['name'],
                image=form['image_url'],
                student_id=form['student_id']
                )
            senior.save()

        client = FaceClient('46675e3d05934138bcb4e9b93880e959', 'a62bca207a57467784f86e37a4241b2a')
        response = client.faces_detect(form['image_url'])
        tid = response['photos'][0]['tags'][0]['tid']
        client.tags_save(tids=tid, uid=form['student_id']+'@senior', label=form['student_id'])
        result = client.faces_train(form['student_id']+'@senior')

        return render(request, 'software/training_result.html', {'result': result})

    else:
        return HttpResponseForbidden('Allowed via POST')


@login_required
def rank(request):
    return render(request, 'software/rank.html', {})