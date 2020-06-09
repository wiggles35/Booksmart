from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class AddBookForm(forms.Form):
    #new_email = forms.EmailField(label='Please use your ND/SMC email')
    #new_seller_name = forms.CharField(label='Your Name')
    new_price = forms.IntegerField(label='Asking Price')
    new_isbn = forms.IntegerField(label='ISBN Number(IF YOU ONLY HAVE AN ISBN-13, PUT "1". IF ISBN-10 PUT THE ISBN)')
    new_class_name = forms.CharField(label='Class Name')
    new_book_name = forms.CharField(label='Book Title')
    new_promise_box = forms.BooleanField(label="I promise to update my listing if it sells")


class RemoveBookForm(forms.Form):
    sale_price = forms.IntegerField(label='How much did your book sell for? Put 0 if did not sell')
    end_promise_box = forms.BooleanField(
        label="Confirm you want to take down posting\n")
    comments = forms.CharField(widget=forms.Textarea,
                               label="What has your experience been with this service? I'd love to hear any and all "
                                     "feedback from how the website worked for you, to the physical buying/selling "
                                     "experience!")


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class CustomUserChangeForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)