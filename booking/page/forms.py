from .models import BookingItem
from django import forms


class BookingSearchForm(forms.Form):
    search_text = forms.CharField(
                    required = False,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Search Item or Venue or User!'})
                  )