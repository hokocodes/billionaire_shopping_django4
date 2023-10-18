from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.template import RequestContext
import requests
from bs4 import BeautifulSoup as bs
from .models import Item

# Create your views here.

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def home(request):
    images2 = []
    if request.method == 'POST':
        url_link = request.POST['url_link']
        r = requests.get(url_link, headers=HEADERS)
        soup = bs(r.content, "lxml")
        images = soup.find_all('img',{"src":True})
        for image in images:
            images2.append(image['src'])
            print(image['src'])
        # images2 = images[0].src


    return render(request, 'home.html', {'images': images2})

def logout_view(request):
    logout(request)
    return redirect('home.html')