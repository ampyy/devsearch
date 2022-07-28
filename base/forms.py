from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.fields import RichTextField


class UpdateProfile(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name ?'}),
                           label='Name')
    profile_picture = forms.ImageField()
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location ?'}),
                               label='Your Location')
    about_yourself = forms.TextInput()
    profession = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Profession ?'}),
                                 label='Your Profession', required=False)
    instagram_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Instagram link ?'}),
                                     label='Your Instagram Link', required=False)
    linkedin_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Linkedin link ?'}),
                                    label='Your Linkedin Link', required=False)
    github_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Github link ?'}),
                                  label='Your Github Link')
    portfolio_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Portfolio link ?'}),
                                     label='Your Portfolio Link', required=False)

    class Meta:
        model = UserProfile
        fields = ('name', 'profile_picture', 'location', 'about_yourself', 'profession',
                  'instagram_link', 'linkedin_link', 'github_link', 'portfolio_link')


class CreateProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = UserProfile.objects.filter(
            user=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    thumbnail = forms.ImageField()
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Name'}),
        label='Your Project Name')
    tagline = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Brief'}),
        label='Your Project Brief')
    description = RichTextField()

    class Meta:
        model = Projects
        fields = ('user', 'thumbnail', 'title', 'tagline', 'description',)


class UpdateProjectForm(forms.ModelForm):
    thumbnail = forms.ImageField()
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Name'}),
        label='Your Project Name')
    tagline = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Project Brief'}),
        label='Your Project Tagline')
    description = RichTextField()
    techstack = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Project techStack comma seperated...'}),
        label='tech Stack')
    github_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Project Github link?'}),
        label='Github link', required=False)
    live_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Project Hosted link?'}),
                                  label='Hosted link', required=False)

    class Meta:
        model = Projects
        fields = ('thumbnail', 'title', 'tagline', 'description','techstack', 'github_link', 'live_link')


class CreateSkillForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateSkillForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = UserProfile.objects.filter(
            user=self.request.user)

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
