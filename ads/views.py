from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from ads.models import Ad, City
from home.models import Data

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Ad
from .forms import AdForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Class Based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def register(request, *args, **kwargs):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('ads:ad_list')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'account/signup.html', context)

class AdListView(LoginRequiredMixin, ListView):
    model = Ad
    context_object_name = 'ads'

    def get_queryset(self):
        new_context = Ad.objects.filter(
            user=self.request.user.username,
        )
        return new_context


class AdDetailView(LoginRequiredMixin, DetailView):
    model = Ad

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    success_url = reverse_lazy('ads:ad_list')

class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    form_class = AdForm
    success_url = reverse_lazy('ads:ad_list')

class AdDeleteView(LoginRequiredMixin, DeleteView):
    model = Ad
    success_url = reverse_lazy('ads:ad_list')


# Create your views here.
def home(request):
    c = City.objects.filter(parent_city=None).order_by('?')
    cg_ad_count = Ad.objects.filter(profile_status="Call Girls").count()
    es_ad_count = Ad.objects.filter(profile_status="Escorts").count()
    meta_title = Data.objects.get(key='home_meta_title').value.replace('%cg_ad_count', str(cg_ad_count)).replace('<p>', '').replace('</p>', '').replace('%es_ad_count', str(es_ad_count))
    meta_description = Data.objects.get(key='home_meta_description').value
    site_name = Data.objects.get(key='site_name').value
    site_logo = Data.objects.get(key='site_logo')
    page_content = Data.objects.get(key='home_content').value
    context = {
        'cities': c,
        'meta_title': meta_title, 
        'meta_description': meta_description,
        'site_logo': site_logo,
        'site_name': site_name,
        'page_content': page_content
    }
    if request.POST:
        url = request.POST.get('url')
        request.session["accepted_cookies"] = True
        print(request.session["accepted_cookies"])
        return redirect(url)
    else:
        try:
            print(request.session["accepted_cookies"])
        except Exception as e:
            request.session["accepted_cookies"] = False
        return render(request, 'home.html', context)


# Create your views here.
def all(request):
    c = City.objects.all().order_by('?')
    cg_ad_count = Ad.objects.filter(profile_status="Call Girls").count()
    es_ad_count = Ad.objects.filter(profile_status="Escorts").count()
    meta_title = Data.objects.get(key='home_meta_title').value.replace('%cg_ad_count', str(cg_ad_count)).replace('<p>', '').replace('</p>', '').replace('%es_ad_count', str(es_ad_count))
    meta_description = Data.objects.get(key='home_meta_description').value
    site_name = Data.objects.get(key='site_name').value
    site_logo = Data.objects.get(key='site_logo')
    page_content = Data.objects.get(key='home_content').value
    context = {
        'cities': c,
        'meta_title': meta_title, 
        'meta_description': meta_description,
        'site_logo': site_logo,
        'site_name': site_name,
        'page_content': page_content
    }
    if request.POST:
        url = request.POST.get('url')
        request.session["accepted_cookies"] = True
        print(request.session["accepted_cookies"])
        return redirect(url)
    else:
        try:
            print(request.session["accepted_cookies"])
        except Exception as e:
            request.session["accepted_cookies"] = False
        return render(request, 'home.html', context)