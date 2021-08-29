from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 

import uuid

from .models import Url

# Create your views here.
def home(request):
    return render(request, "shortner/home.html")

def createUrl(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        uid = str(uuid.uuid4())[:5]
        newUrl = Url(link=url, uuid=uid)
        newUrl.save()

        return render(request, "shortner/shorten-url.html", {'uid' : uid})

def browse(request, pk):
    urlDetails = Url.objects.get(uuid=pk)
    return redirect(urlDetails)
