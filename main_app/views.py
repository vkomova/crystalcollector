from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsesForm
import uuid
import boto3
from .models import Crystal, Country, Uses, Photo

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'crystalcollector'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def crystals_index(request):
  crystals = Crystal.objects.filter(user=request.user)
  return render(request, 'crystals/index.html', { 'crystals': crystals })

@login_required
def crystals_detail(request, crystal_id):
  crystal = Crystal.objects.get(id=crystal_id)
  countries_crystal_doesnt_have = Country.objects.exclude(id__in = crystal.countries.all().values_list('id'))
  uses_form = UsesForm()
  return render(request, 'crystals/detail.html', { 
    'crystal': crystal, 'uses_form': uses_form,
    'countries': countries_crystal_doesnt_have
  })

@login_required
def add_uses(request, crystal_id):
  form = UsesForm(request.POST)
  if form.is_valid():
    new_uses = form.save(commit=False)
    new_uses.crystal_id = crystal_id
    new_uses.save()
  return redirect('detail', crystal_id=crystal_id)

class CrystalCreate(LoginRequiredMixin, CreateView):
  model = Crystal
  fields = ['name', 'type', 'description', 'healingproperties']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CrystalUpdate(LoginRequiredMixin, UpdateView):
  model = Crystal
  fields = ['name', 'type', 'description', 'healingproperties']

class CrystalDelete(LoginRequiredMixin, DeleteView):
  model = Crystal
  success_url = '/crystals/'

class CountryList(LoginRequiredMixin, ListView):
  model = Country

class CountryDetail(LoginRequiredMixin, DetailView):
  model = Country

class CountryCreate(LoginRequiredMixin, CreateView):
  model = Country
  fields = '__all__'

class CountryUpdate(LoginRequiredMixin, UpdateView):
  model = Country
  fields = ['name', 'color']

class CountryDelete(LoginRequiredMixin, DeleteView):
  model = Country
  success_url = '/countries/'

@login_required
def assoc_country(request, crystal_id, country_id):
  Crystal.objects.get(id=crystal_id).countries.add(country_id)
  return redirect('detail', crystal_id=crystal_id)

@login_required
def unassoc_country(request, crystal_id, country_id):
  Crystal.objects.get(id=crystal_id).countries.remove(country_id)
  return redirect('detail', crystal_id=crystal_id)

@login_required
def add_photo(request, crystal_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, crystal_id=crystal_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', crystal_id=crystal_id)