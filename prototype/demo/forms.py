from django import forms


class AddBookForm(forms.Form):
    new_email = forms.EmailField(label='Please use your ND/SMC email')
    new_seller_name = forms.CharField(label='Your Name')
    new_price = forms.IntegerField(label='Asking Price')
    new_isbn = forms.IntegerField(label='ISBN Number')
    new_class_name = forms.CharField(label='Class Name')
    new_book_name = forms.CharField(label='Book Title')
    new_phone_number = forms.IntegerField(label='Phone Number')
    new_promise_box = forms.BooleanField(label="I promise to update my listing if it sells")


