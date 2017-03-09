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
def mypocket(request, pk):

    user = User.objects.get(pk=pk) 
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = request.POST
	
        if form.get('not_recongnized', False):
            catching = Catching.objects.get(pk=form['catching'])
            catching.in_recognized = False

        else:
            senior = Senior.objects.get(student_id=form['student_id'])
            ex_catching = Catching.objects.filter(profile=profile).filter(senior=senior).filter(is_in_pocket=True)
            if ex_catching:
                ex_catching[0].is_in_pocket = False
                ex_catching[0].save()
                senior.caught_count -= 1
                profile.catching_count -= 1

            senior.caught_count += 1
            senior.save()

            profile.catching_count += 1
            profile.save()

            catching = Catching.objects.filter(profile=profile).filter(senior=None).order_by('-registered_time')[0]

            catching.comment = form['comment']
            catching.senior = senior
            catching.is_in_pocket = True
            catching.save()

    if profile.is_freshman:
        catching_count = profile.catching_count
        catching_list = Catching.objects.filter(profile=profile).filter(is_in_pocket=True)
    else:
        senior = Senior.objects.get(student_id=profile.user.username)
        catching_count = senior.caught_count
        catching_list = Catching.objects.filter(senior=senior).filter(is_in_pocket=True)

    return render(request, 'software/mypocket.html', {'user_name': user.first_name,
                                                      'catching_list': catching_list,
                                                      'catching_count': catching_count})

@login_required
def catching(request, spk, cpk):
    catching = Catching.objects.get(pk=cpk)

    if request.method == 'POST':
        user = request.user
        form = request.POST
        chatting = Chatting.objects.create(
            profile = Profile.objects.get(user=user),
            chat=form['chat'],
            catching = catching
            )
        catching.chatting_count += 1
        catching.save()
    
    chatting_list = Chatting.objects.filter(catching=catching).order_by('-modified_time')
    return render(request, 'software/catching.html', {'catching': catching, 'chatting_list': chatting_list})


@login_required
def catchsenior(request):
    u1 = request.user
    profile = Profile.objects.get(user=u1)
    if profile.is_freshman == True:
        return render(request, 'software/catchsenior.html', {})
    else:
        return render(request, 'software/catchsenior.html', {'senior': profile})

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

            student_id1 = result['photos'][0]['tags'][0]['uids'][0]['uid'].split('@')[0]
            confidence1 = result['photos'][0]['tags'][0]['uids'][0]['confidence']
            senior1 = Senior.objects.get(student_id=student_id1)
            senior1_name = senior1.name

            student_id2 = result['photos'][0]['tags'][0]['uids'][1]['uid'].split('@')[0]
            confidence2 = result['photos'][0]['tags'][0]['uids'][1]['confidence']
            senior2 = Senior.objects.get(student_id=student_id2)
            senior2_name = senior2.name

            student_id3 = result['photos'][0]['tags'][0]['uids'][2]['uid'].split('@')[0]
            confidence3 = result['photos'][0]['tags'][0]['uids'][2]['confidence']
            senior3 = Senior.objects.get(student_id=student_id3)
            senior3_name = senior3.name          

            return render(request, 'software/recognize.html', {'catching': catching,
                                                               'image_url': image_url,
                                                               'senior1_name': senior1_name,
                                                               'confidence1': confidence1,
                                                               'student_id1': student_id1,
                                                               'senior2_name': senior2_name,
                                                               'confidence2': confidence2,
                                                               'student_id2': student_id2,
                                                               'senior3_name': senior3_name,
                                                               'confidence3': confidence3,
                                                               'student_id3': student_id3,
                                                              })
        else:
            return HttpResponseForbidden('form is invalid')

    else:
        return HttpResponseForbidden('Allowed via POST')



@login_required
def senior(request, pk):
    if request.method == 'POST':        
        user = request.user
        profile = Profile.objects.get(user=user)
        form = request.POST
        catching = Catching.objects.get(pk=form['catching'])

        if form.get('like', False):
            if not Like.objects.filter(catching=catching).filter(profile=profile):
                Like.objects.create(
                    profile=profile,
                    catching=catching
                    )
                catching.like_count += 1
                catching.save()

        elif form.get('singo', False):
            if not Singo.objects.filter(catching=catching).filter(profile=profile):
                Singo.objects.create(
                    profile=profile,
                    catching=catching
                    )   
                catching.singo_count += 1
                catching.save()

    senior = get_object_or_404(Senior, pk=pk)
    catching_list = Catching.objects.filter(senior=Senior.objects.get(pk=pk)).filter(is_in_pocket=True)
    return render(request, 'software/senior.html', {'senior': senior, 'catching_list' : catching_list})


@login_required
def seniors(request):

    form = request.GET
    if form.get('searched_name', False):
        seniors = Senior.objects.filter(name__contains=form['searched_name'])

    else:
        seniors = Senior.objects.all()
    return render(request, 'software/seniors.html', {'seniors' : seniors})


@login_required
def seniors_search(request):
    result = request.GET['searched_name']
    seniors = Senior.objects.filter(name=result)
    return render(request, 'software/seniors.html', {'seniors': seniors})


@login_required
def training(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden('Only for Superuser')

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

            return render(request, 'software/training.html', {'result': result})

        else:
            return HttpResponseForbidden('form is invalid')

    else:
        return render(request, 'software/training.html', {})


@login_required
def rank_freshman(request):

    form = request.GET

    if form.get('searched_name', False):
        user_list = User.objects.filter(first_name__contains=form['searched_name'])
        p_list = []
        for user in user_list:
            profile = Profile.objects.get(user=user)
            p_list.insert(0, profile)
        profile_list = sorted(p_list, key=lambda x: x.catching_count, reverse=True)
    else:
        profile_list = Profile.objects.filter(is_freshman=True).order_by('-catching_count')
    
    return render(request, 'software/rank_freshman.html', {'profile_list': profile_list})


@login_required
def rank_senior(request):

    form = request.GET

    if form.get('searched_name', False):
        senior_list = Senior.objects.filter(name__contains=form['searched_name']).order_by('-caught_count')
    else:
        senior_list = Senior.objects.order_by('-caught_count')
    
    return render(request, 'software/rank_senior.html', {'senior_list': senior_list})

