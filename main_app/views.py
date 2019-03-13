from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import UsesForm
import uuid
import boto3
from .models import Crystal, Country, Uses, Photo

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'crystalcollector'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crystals_index(request):
  crystals = Crystal.objects.all()
  return render(request, 'crystals/index.html', { 'crystals': crystals })

def crystals_detail(request, crystal_id):
  crystal = Crystal.objects.get(id=crystal_id)
  countries_crystal_doesnt_have = Crystal.objects.exclude(id__in = crystal.countries.all().values_list('id'))
  uses_form = UsesForm()
  return render(request, 'crystals/detail.html', { 
    'crystal': crystal, 'uses_form': uses_form,
    'countries': countries_crystal_doesnt_have
  })

def add_uses(request, crystal_id):
  form = UsesForm(request.POST)
  if form.is_valid():
    new_uses = form.save(commit=False)
    new_uses.crystal_id = crystal_id
    new_uses.save()
  return redirect('detail', crystal_id=crystal_id)

class CrystalCreate(CreateView):
  model = Crystal
  fields = '__all__'

class CrystalUpdate(UpdateView):
  model = Crystal
  fields = ['name', 'type', 'description', 'healingproperties']

class CrystalDelete(DeleteView):
  model = Crystal
  success_url = '/crystals/'

class CountryList(ListView):
  model = Country

class CountryDetail(DetailView):
  model = Country

class CountryCreate(CreateView):
  model = Country
  fields = '__all__'

class CountryUpdate(UpdateView):
  model = Country
  fields = ['name', 'color']

class CountryDelete(DeleteView):
  model = Country
  success_url = '/countries/'

def assoc_country(request, crystal_id, country_id):
  Crystal.objects.get(id=crystal_id).countries.add(country_id)
  return redirect('detail', crystal_id=crystal_id)

def unassoc_country(request, crystal_id, country_id):
  Crystal.objects.get(id=crystal_id).countries.remove(country_id)
  return redirect('detail', crystal_id=crystal_id)

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