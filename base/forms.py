from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.fields import RichTextField


class UpdateProfile(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name ?'}),
                           label='Name')

    class Meta:
        model = UserProfile
        fields = ('name', )


class CreateProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    thumbnail = forms.ImageField()
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Name'}),
        label='Your Project Name')
    brief = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Name'}),
        label='Your Project Name')
    description = RichTextField()

    class Meta:
        model = Projects
        fields = ('user', 'thumbnail', 'title', 'brief', 'description',)


class CreateSkillForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateSkillForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Name'}),
        label='Your Project Name')
    brief = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Name'}),
        label='Your Project Name')

    class Meta:
        model = Skill
        fields = ('user', 'title', 'brief',)