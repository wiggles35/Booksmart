from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Listing


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, demo_id):
    return HttpResponse("You're looking at item %s." % demo_id)


def index(request):
    latest_listing_list = Listing.objects.order_by('seller_name')[:5]
    context = {'latest_listing_list': latest_listing_list}
    return render(request, 'demo/index.html', context)
