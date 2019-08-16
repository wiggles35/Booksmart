from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Listing
from .forms import AddBookForm


def home(request):
    latest_listing_list = Listing.objects.order_by('seller_name')
    context = {'latest_listing_list': latest_listing_list}
    return render(request, 'demo/home.html', context)


def about_us(request):
    return render(request, 'demo/about_us.html')


def add_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddBookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_book = Listing(isbn=form.cleaned_data['new_isbn'], class_name=form.cleaned_data['new_class_name'],
                               book_name=form.cleaned_data['new_book_name'],
                               seller_name=form.cleaned_data['new_seller_name'], price=form.cleaned_data['new_price'])
            new_book.save()
            return HttpResponseRedirect('/demo')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddBookForm()

    return render(request, 'demo/add_book.html', {'form': form})
