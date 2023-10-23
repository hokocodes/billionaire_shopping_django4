import json
from django.http import HttpResponseServerError, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.template import RequestContext
import requests
from bs4 import BeautifulSoup as bs
from .models import Item
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyData
from .serializers import MyDataSerializer

# Create your views here.

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def home(request):
    images1 = []
    images2 = []
    bookimgs = []
    if request.method == 'POST':

        images2 = []
        homeurl = request.POST.get('url_link')
        bookurl = request.POST.get('url')
        # if homeurl != None and homeurl != '':
        #     rh = requests.get(homeurl, headers=HEADERS)
        #     soup = bs(rh.content, "lxml")
        #     images11 = soup.find_all('img',{"src":True})
        #     images1.clear()
        #     for image in images11:
        #         images1.append(image['src'])
        if bookurl:
            rb = requests.get(bookurl, headers=HEADERS)
            soupb = bs(rb.content, 'lxml')
            images22 = soupb.find_all('img',{"src":True})
            for image in images22:
                images2.append(image['src'])
            
            images2 = [image['src'] for image in images22]
            request.session['images2'] = images2
            return JsonResponse({'bookimgs': images2})
    
    bookimgs = request.session.get('images2', [])
    print('outside')
    print(bookimgs)
    return render(request, 'home.html', {'bookimgs': bookimgs})
    

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



# class MyDataAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = MyDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def mydata_view(request):
    if request.method == 'POST':
        try:
            data = request.POST.get('test')
            # Process the data as needed
            print(data)
            return JsonResponse(data)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data', 'test': test}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)