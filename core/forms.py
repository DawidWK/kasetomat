from django import forms
from core.models import Kaseta, Order

class KasetaForm(forms.ModelForm):
    class Meta:
        model = Kaseta
        fields = ["title", "release_date", "duration", "price", "availability"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['release_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})


class CartForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone' ]