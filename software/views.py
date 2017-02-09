from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect

from .forms import ImageUploadForm
from .models import Senior

#from catchme.settings import AWS_ACCESS_KEY, AWS_SECRET_KEY, S3_BUCKET, REGION_NAME
import boto3
from boto3.session import Session

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
                #image = form.cleaned_data['image']
            )
            s.save()
            image_to_upload = request.FILES.get('image')


            cloudFilename = 'software/' + image_to_upload.name
            s3 = boto3.resource('s3')
            s3.Bucket('catchmesoongsil').put_object(Key=cloudFilename, Body=image_to_upload)

            s3_client = boto3.client('s3')

            #url = s3_client.generate_url(expires_in=0, query_auth=False, force_http=True)


            url = s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': 'catchmesoongsil/software',
                    'Key': image_to_upload.name
                }
            )

            return HttpResponse(url)

            #client = FaceClient('f2f4e3c754f940598fe1d5c3cfd8f626', '04632fe53d33463cb8dabeb0ccc6df64')
            #image_url = url
            #result = client.faces_recognize("esmond", image_url, namespace='senior')
            #return render(request, 'software/recognize.html', {'result': image_url})

            #client = FaceClient('f2f4e3c754f940598fe1d5c3cfd8f626', '04632fe53d33463cb8dabeb0ccc6df64')
            #image_url = 'http://192.168.1.21:8000' + s.image.url
            #result = client.faces_recognize("esmond", image_url, namespace='senior')
            #return render(request, 'software/recognize.html', {'result': image_url})

        return HttpResponseForbidden("form is invalid")
    else:
        return HttpResponseForbidden("allowed via POST")

def rank(request):
    return render(request, 'software/rank.html', {})