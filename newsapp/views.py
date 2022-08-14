from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
import requests
import http.client, urllib.parse

def home(request):
    return render(request,'newsapp/index.html')


def news(request):
    country = request.GET.get('country')

    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=d67ba7e4ae6648d18a02deba84a9b8b7'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    news = {
        'articles': articles
    }

    return render(request, 'newsapp/news.html', news)

class SignupView(View):
    def get(self, request):
        fm = SignUpForm()
        return render(request, 'newsapp/signup.html', {'form':fm})

    def post(self,request):
        fm = SignUpForm(request.POST)

        if fm.is_valid():
            messages.success(request, "Signup Successful!")
            fm.save()
            return redirect('/signup')
        else:
            # messages.error(request, "Oops Error!")
            return render(request, 'newsapp/signup.html', {'form': fm})

class MyloginView(View):
    def get(self,request):
        fm = MyLoginForm()
        return render(request,'newsapp/login.html',{'form':fm})

    def post(self,request):
        fm = MyLoginForm(request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/news')
        else:
            messages.error(request, "Please Sign Up first!")
            return redirect('/login')


