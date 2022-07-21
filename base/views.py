from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from .models import *
from .forms import *
from django.db.models import Q


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base/index.html")
    

def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    projects = Projects.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)
    return render(request, "base/profile.html", {'profile' : profile, 'projects':projects, 'skills' : skills})


def update_profile(request, slug):
    context = {}
    obj = get_object_or_404(UserProfile, uuid=slug)
    form = UpdateProfile(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('index')
    context["form"] = form
    context["user"] = obj.user
    return render(request, 'base/edit_profile.html', context)


class ProjectsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Projects
    form_class = CreateProjectForm
    template_name = 'base/add_project.html'

    def get_success_url(self):
        return reverse('profile')

    def get_form_kwargs(self):
        kwargs = super(ProjectsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def project_detail(request, slug):
    project = Projects.objects.get(uuid=slug)
    return render(request, "base/project_details.html", {'project':project})


class SkillsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Skill
    form_class = CreateSkillForm
    template_name = 'base/add_skill.html'

    def get_success_url(self):
        return reverse('profile')

    def get_form_kwargs(self):
        kwargs = super(SkillsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs