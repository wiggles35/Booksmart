from django import forms


class AddBookForm(forms.Form):
    new_email = forms.EmailField(label='Please use your ND/SMC email')
    new_seller_name = forms.CharField(label='Your Name')
    new_price = forms.IntegerField(label='Asking Price')
    new_isbn = forms.IntegerField(label='ISBN Number')
    new_class_name = forms.CharField(label='Class Name')
    new_book_name = forms.CharField(label='Book Title')
    new_promise_box = forms.BooleanField(label="I promise to update my listing if it sells")


class RemoveBookForm(forms.Form):
    sale_price = forms.IntegerField(label='How much did your book sell for? Put 0 if did not sell')
    end_promise_box = forms.BooleanField(
        label="I promise that I am removing ONLY an entry that I put up. This website operates on the honor system\n")
    comments = forms.CharField(widget=forms.Textarea,
                               label="What has your experience been with this service? I'd love to hear any and all feedback from how the website worked for you, to the physical buying/selling experience!")
