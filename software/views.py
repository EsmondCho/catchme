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

        ex_catching = Catching.objects.filter(profile=profile).filter(senior=senior).filter(is_in_pocket=True)
        if ex_catching:
            ex_catching[0].is_in_pocket = False

        catching = Catching.objects.filter(profile=profile).filter(senior=senior)[0]
        catching.comment = form['comment']
        catching.senior = senior
        catching.is_in_pocket = True
        catching.save()

    catching_count = profile.catching_count
    catching_list = Catching.objects.filter(profile=profile).filter(is_in_pocket=True)

    return render(request, 'software/mypocket.html', {'catching_list': catching_list,
                                                      'catching_count': catching_count})


@login_required
def catching(request, pk):
    if request.method == 'POST':
        form = request.POST
        chatting = Chatting.objects.create(
      #      name=form['name'],
            chat=form['chat'],
            catching = Catching.objects.get(pk=pk)
            )

    c = get_object_or_404(Catching, pk=pk)
    catching = Catching.objects.get(pk=pk)
    chatting_list = Chatting.objects.filter(catching=catching)
    return render(request, 'software/catching.html', {'catching': catching, 'chatting_list': chatting_list})


@login_required
def catchsenior(request):
    return render(request, 'software/catchsenior.html', {})


@login_required
def recognize(request):

    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)

        f = request.POST
        form = ImageUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            catching = Catching.objects.create(
                image=form.cleaned_data['image'],
                senior=None,
                profile=profile,
                comment=""
            )
            catching.save()

            image_url = 'http://150.95.135.222:8000' + catching.image.url
            
            client = FaceClient('46675e3d05934138bcb4e9b93880e959', 'a62bca207a57467784f86e37a4241b2a')
            result = client.faces_recognize('all', image_url, namespace='senior')

            student_id = result['photos'][0]['tags'][0]['uids'][0]['uid'].split('@')[0]
            confidence = result['photos'][0]['tags'][0]['uids'][0]['confidence']

            if Senior.objects.filter(student_id=student_id):
                senior = Senior.objects.get(student_id=student_id)
                senior_name = senior.name

                catching.senior = senior
                catching.save()

                return render(request, 'software/recognize.html', {'senior_name': senior_name,
                                                                   'image_url': image_url,
                                                                   'confidence': confidence,
                                                                   'student_id': student_id
                                                                   })
            else:
                return HttpResponseForbidden(student_id + ' This person is not in jigabmon')
        else:
            return HttpResponseForbidden('form is invalid')

    else:
        return HttpResponseForbidden('Allowed via POST')



@login_required
def senior(request, pk):
    senior = get_object_or_404(Senior, pk=pk)
    catching_list = Catching.objects.filter(senior=Senior.objects.get(pk=pk)).filter(is_in_pocket=True)
    return render(request, 'software/senior.html', {'senior': senior, 'catching_list' : catching_list})


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

        f = request.POST
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            if not Senior.objects.filter(student_id=f['student_id']):
                senior = Senior.objects.create(
                    name=f['name'],
                    image=form.cleaned_data['image'],
                    student_id=f['student_id']
                    )
                senior.save()
            else:
                senior = Senior.objects.get(student_id=f['student_id'])
                senior.image = form.cleaned_data['image']
                senior.save()

            image_url = 'http://150.95.135.222:8000' + senior.image.url

            client = FaceClient('46675e3d05934138bcb4e9b93880e959', 'a62bca207a57467784f86e37a4241b2a')
            response = client.faces_detect(image_url)
            tid = response['photos'][0]['tags'][0]['tid']
            client.tags_save(tids=tid, uid=f['student_id']+'@senior', label=f['student_id'])
            result = client.faces_train(f['student_id']+'@senior')

            return render(request, 'software/training_result.html', {'result': result})

        else:
            return HttpResponseForbidden('form is invalid')

    else:
        return HttpResponseForbidden('Allowed via POST')


@login_required
def rank(request):
    return render(request, 'software/rank.html', {})
