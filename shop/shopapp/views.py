from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.

def home(request):
    if request.method == 'POST':
        url_link = request.POST['url_link']
        r = requests.get(url_link)
        soup = bs(r.content)
        images = soup.find_all('img')
        for image in images:
            print(image['src'])

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')