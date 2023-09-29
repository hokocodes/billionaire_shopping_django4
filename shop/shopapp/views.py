from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests
from bs4 import BeautifulSoup as bs
from .models import Item

# Create your views here.

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def home(request):
    if request.method == 'POST':
        try: 
            url_link = request.POST['url_link']
            r = requests.get(url_link, headers=HEADERS)
            soup = bs(r.content, "lxml")
            images = soup.find_all('img')
            images2 = []
            for image in images:
                images2.append(image['src'])
                print(image['src'])
        except: 
            pass

    return render(request, 'home.html', {'images': images2})

def logout_view(request):
    logout(request)
    return redirect('/')