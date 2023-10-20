import json
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
        homeurl = request.POST['url_link']
        rh = requests.get(homeurl, headers=HEADERS)
        soup = bs(rh.content, "lxml")
        images = soup.find_all('img',{"src":True})
        appendimages(images, images2)
    elif request.method == 'GET':
        bookurl = request.GET.get('url')
        if bookurl == True:
            rb = requests.get(bookurl, headers=HEADERS)
            soupb = bs(rb.content, 'lxml')
            images = soupb.find_all('img',{"src":True})
            appendimages(images, images2)
        else: 
            pass

    return render(request, 'home.html', {'images': images2})

def logout_view(request):
    logout(request)
    return redirect('home.html')

def bookmarklet(request):
    images3 = []
    if request.method == 'GET':
        bookurl = request.GET.get('url')
        print(bookurl)
        r = requests.get(bookurl, headers=HEADERS)
        soup = bs(r.content, "lxml")
        images = soup.find_all('img',{"src":True})
        for image in images:
            images3.append(image['src'])
            print(image['src'])

    return render(request, 'bookmarklet.html', {'images': images3})

def appendimages(images, arr):
    for image in images:
        arr.append(image['src'])
        print(image['src'])