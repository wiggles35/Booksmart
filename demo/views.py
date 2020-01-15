from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .models import Listing, SoldBook, CustomUser
from .forms import AddBookForm, RemoveBookForm, SignUpForm
from django.contrib.auth.decorators import login_required
import datetime


def home(request):
    latest_listing_list = Listing.objects.order_by('-upload_date')
    context = {'latest_listing_list': latest_listing_list}
    return render(request, 'demo/home.html', context)


@login_required
def start_delete_entry(request, pk):
    end_listing = Listing.objects.get(pk=pk)
    form = RemoveBookForm()
    context = {'end_listing': end_listing, 'form': form}
    return render(request, 'demo/delete_entry.html', context)


@login_required
def finish_delete_entry(request, pk):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RemoveBookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            end_listing = Listing.objects.get(pk=pk)
            new_sale = SoldBook(isbn=end_listing.isbn, class_name=end_listing.class_name,
                                book_name=end_listing.book_name, seller_name=end_listing.seller_name,
                                price=end_listing.price, email=end_listing.email,
                                sold_price=form.cleaned_data['sale_price'],
                                customer_feedback=form.cleaned_data['comments'])
            new_sale.save()
            end_listing.delete()
            return HttpResponseRedirect('/demo')

    return HttpResponseRedirect('/demo')


def about_us(request):
    return render(request, 'demo/about_us.html')


def join_us(request):
    return render(request, 'demo/join_us.html')


@login_required
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
                               user=request.user, price=form.cleaned_data['new_price'],
                               email=request.user.email, upload_date=datetime.datetime.now(), )
            new_book.save()
            return HttpResponseRedirect('/demo')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddBookForm()

    return render(request, 'demo/add_book.html', {'form': form})


@login_required
def my_listings(request):
    listings_by_user = Listing.objects.filter(user=request.user).values()
    context = {'listings_by_user': listings_by_user}
    return render(request, 'demo/my_listings.html', context)


# This displays the finished postings
@login_required
def sold_listings(request):
    finished_listings = SoldBook.objects.order_by('-email')
    context = {'finished_listings': finished_listings}
    return render(request, 'demo/finished_listings.html', context)


