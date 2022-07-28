from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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


class Developers(generic.ListView):
    model = UserProfile
    template_name = 'base/developers.html'
    context_object_name = 'developers'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['developers'] = UserProfile.objects.all()
    #     print(context['developers'])
    #     return context


class ProjectsView(generic.ListView):
    model = Projects
    template_name = 'base/projects.html'
    context_object_name = 'projects'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['developers'] = UserProfile.objects.all()
    #     print(context['developers'])
    #     return context


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    projects = Projects.objects.filter(user=profile)
    skills = Skill.objects.filter(user=profile)
    return render(request, "base/profile.html", {'profile': profile, 'projects': projects, 'skills': skills})


@login_required
def update_profile(request, slug):
    context = {}
    obj = get_object_or_404(UserProfile, uuid=slug)
    if request.method == 'POST':
        form = UpdateProfile(request.POST or None, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfile(instance=obj)
    context["form"] = form
    context["profile_user"] = obj.user
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


@login_required
def update_project(request, slug):
    context = {}
    obj = get_object_or_404(Projects, uuid=slug)
    if request.method == 'POST':
        form = UpdateProjectForm(request.POST or None, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProjectForm(instance=obj)

    context["form"] = form
    str_user = str(obj.user)
    user = str(request.user)
    context['project_user'] = str_user
    context['user'] = user
    return render(request, 'base/edit_project.html', context)


@login_required
def delete_project(request, slug):
    context = {}
    obj = get_object_or_404(Projects, uuid=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('profile')
    str_user = str(obj.user)
    user = str(request.user)
    context['project_user'] = str_user
    context['user'] = user
    return render(request, "base/delete_project.html", context)


def project_detail(request, slug):
    project = Projects.objects.get(uuid=slug)
    return render(request, "base/project_details.html", {'project': project})


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


@login_required
def delete_skill(request, slug):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Skill, uuid=slug)

    if request.method == "POST":
        obj.delete()
        # home page
        return redirect('profile')
    str_user = str(obj.user)
    user = str(request.user)
    context['project_user'] = str_user
    context['user'] = user
    return render(request, "base/delete_skill.html", context)


def user_profile(request, slug):
    profile = UserProfile.objects.get(uuid=slug)
    projects = Projects.objects.filter(user=profile)
    skills = Skill.objects.filter(user=profile)
    return render(request, "base/user_profile.html", {'profile': profile, 'projects': projects, 'skills': skills})


def search_developers(request):
    developers = UserProfile.objects.all()
    query = request.GET.get('q')
    if query:
        developers = developers.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(about_yourself__icontains=query)
        ).distinct()

    context = {
        'developers': developers,
    }
    return render(request, "base/search-developers.html", context)


def search_projects(request):
    projects = Projects.objects.all()
    query = request.GET.get('q')
    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(tagline__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    context = {
        'projects': projects,
    }
    return render(request, "base/search-projects.html", context)