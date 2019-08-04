from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Listing


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, demo_id):
    return HttpResponse("You're looking at item %s." % demo_id)


def home(request):
    latest_listing_list = Listing.objects.order_by('seller_name')
    context = {'latest_listing_list': latest_listing_list}
    return render(request, 'demo/home.html', context)


def add_book(request):
    return render(request, 'demo/add_book.html')


def about_us(request):
    return render(request, 'demo/about_us.html')

