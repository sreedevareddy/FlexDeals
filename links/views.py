from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from links.DataFetch import Fetch_Data
from links.home_scraping import Get_Deals


from django.contrib import messages
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


from bs4 import BeautifulSoup as Soup
import os
from django.conf import settings
import requests


def home_view(request):
    if request.method == "GET":
        a = []
        entry_list = ["electronics","beauty","books","music","mobiles","laptops"]
        for entry in entry_list:
            f = Fetch_Data(entry).Scrap()
            a += f 

    context = {
        'data' : a
    }
    return render(request, 'links/index.html',context)


def scraping(request):
    if request.method == "GET":
        entry = request.GET.get('search')
        f = Fetch_Data(entry)
    
    context = {
        'data' : f.Scrap()
    }
    return render(request,'links/searchpage.html',context)

def entertainment(request):

    entry = "entertainment"
    f = Fetch_Data(entry)
    
    context = {
        'data' : f.Scrap()
    }
    return render(request,'links/searchpage.html',context)

def beauty(request):

    entry = "beauty"
    f = Fetch_Data(entry)
    
    context = {
        'data' : f.Scrap()
    }
    return render(request,'links/searchpage.html',context)

def clothing(request):

    entry = "clothing"
    f = Fetch_Data(entry)
    
    context = {
        'data' : f.Scrap()
    }
    return render(request,'links/searchpage.html',context)


def appliances(request):

    entry = "appliances"
    f = Fetch_Data(entry)
    
    context = {
        'data' : f.Scrap()
    }
    return render(request,'links/searchpage.html',context)

def electronics(request):

    entry = "electronics"
    f = Fetch_Data(entry)
    
    context = {
        'data' : f.Scrap()
    }
    return render(request,'links/searchpage.html',context)