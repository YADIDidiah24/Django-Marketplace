from django import forms
from core.models import Item
input_class = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')

        widgets = {
            'category': forms.Select(attrs={
                'class': input_class
            }),
            'name': forms.TextInput(attrs={
                'class': input_class
            }),
            'description': forms.Textarea(attrs={
                'class': input_class
            }),
            'price': forms.TextInput(attrs={
                'class': input_class
            }),
            'Image': forms.FileInput(attrs={
                'class': input_class
            }),
        }     


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': input_class
            }),
            'description': forms.Textarea(attrs={
                'class': input_class
            }),
            'price': forms.TextInput(attrs={
                'class': input_class
            }),
            'Image': forms.FileInput(attrs={
                'class': input_class
            }),
                'is_sold': forms.Select(attrs={
                'class': input_class
            }),
        }     