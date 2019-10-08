from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .models import Listing, SoldBook
from .forms import AddBookForm, RemoveBookForm, SignUpForm
import datetime


def home(request):
    latest_listing_list = Listing.objects.order_by('-upload_date')
    context = {'latest_listing_list': latest_listing_list}
    return render(request, 'demo/home.html', context)


def start_delete_entry(request, pk):
    end_listing = Listing.objects.get(pk=pk)
    form = RemoveBookForm()
    context = {'end_listing': end_listing, 'form': form}
    return render(request, 'demo/delete_entry.html', context)


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/demo/')
    else:
        form = SignUpForm()
    return render(request, 'demo/signup.html', {'form': form})


def about_us(request):
    return render(request, 'demo/about_us.html')


def join_us(request):
    return render(request, 'demo/join_us.html')


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
                               seller_name=form.cleaned_data['new_seller_name'], price=form.cleaned_data['new_price'],
                               email=form.cleaned_data['new_email'], upload_date=datetime.datetime.now())
            new_book.save()
            return HttpResponseRedirect('/demo')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddBookForm()

    return render(request, 'demo/add_book.html', {'form': form})
