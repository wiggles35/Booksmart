from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('about_us/', views.about_us, name='about_us'),
    path('join_us/', views.join_us, name='join_us'),
    path('delete_entry/(<pk>[0-9]+)/', views.start_delete_entry, name='start_delete_entry'),
    path('delete_entry/(<pk>[0-9]+)/delete/', views.finish_delete_entry, name='finish_delete_entry'),
    path('signup/', views.signup, name='signup'),
]

