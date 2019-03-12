from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Crystal
from .forms import UsesForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crystals_index(request):
  crystals = Crystal.objects.all()
  return render(request, 'crystals/index.html', { 'crystals': crystals })

def crystals_detail(request, crystal_id):
  crystal = Crystal.objects.get(id=crystal_id)
  uses_form = UsesForm()
  return render(request, 'crystals/detail.html', { 
    'crystal': crystal, 'uses_form': uses_form
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