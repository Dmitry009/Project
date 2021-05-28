<<<<<<< Updated upstream
import os
from uuid import uuid4

from django import forms
from django.forms import fields
=======
from django import forms
>>>>>>> Stashed changes
from .models import Event, UserMessages, Category, Dish


class UserMessageForm(forms.ModelForm):
    user_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Name', 'required': 'required'}))
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'id': 'email',
                                                                'class': 'form-control',
                                                                'placeholder': 'Email',
                                                                'required': 'required'}))
    message = forms.CharField(max_length=200,
                              widget=forms.Textarea(
                                  attrs={'name': 'message', 'id': 'message', 'class': 'form-control',
                                         'rows': '4', 'placeholder': 'Your lovely message',
                                         'required': 'required'}))

    class Meta:
        model = UserMessages
        fields = ('user_name', 'user_email', 'message')


class CreateCategory(forms.ModelForm):
    title = forms.CharField(max_length=50)
    category_order = forms.IntegerField()
    is_visible = forms.CheckboxInput()
    is_special = forms.CheckboxInput()
<<<<<<< Updated upstream
    photo = forms.ImageField()
=======
>>>>>>> Stashed changes

    class Meta:
        model = Category
        fields = (
            'title',
            'category_order',
            'is_visible',
            'is_special',
<<<<<<< Updated upstream
            'photo'
=======
>>>>>>> Stashed changes
        )


class CreateDish(forms.ModelForm):
    title = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=7, decimal_places=2)
    is_visible = forms.CheckboxInput()
<<<<<<< Updated upstream
    is_special = forms.CheckboxInput()
=======
>>>>>>> Stashed changes
    description = forms.CharField(max_length=300,
                                  widget=forms.Textarea(
                                      attrs={'name': 'description', 'id': 'id_description',
                                             'rows': '4'}))
    photo = forms.ImageField()
<<<<<<< Updated upstream
    #category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
=======
>>>>>>> Stashed changes

    class Meta:
        model = Dish
        fields = [
            'title',
            'price',
            'is_visible',
<<<<<<< Updated upstream
            'is_special',
=======
>>>>>>> Stashed changes
            'description',
            'photo',
            'category'
        ]


class CreateEvent(forms.ModelForm):
    title = forms.CharField(max_length=50)
    photo = forms.ImageField()
    description = forms.CharField(max_length=300,
                                  widget=forms.Textarea(
                                      attrs={'name': 'description', 'id': 'id_description',
                                             'rows': '4'}))
    event_date = forms.DateField()
    event_time = forms.TimeField()
    price = forms.DecimalField()

    class Meta:
        model = Event
        fields = [
            "title",
            "photo",
            "description",
            "event_date",
            "event_time",
            "price"
        ]
