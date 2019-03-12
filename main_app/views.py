from django.shortcuts import render
from django.http import HttpResponse
from .models import Crystal

def home(request):
    return HttpResponse('<h1>╲┏━┳━━━━━━━━┓╲╲<br>╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲<br>╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲<br>╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲<br>╲┃◯┃╭╮╰╯┏━━━┳╯╲<br>╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲<br>╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲</h1>')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    crystals = Crystal.objects.all()
    return render(request, 'crystals/index.html', { 'crystals': crystals })

def crystals_detail(request, crystal_id):
  crystal = Crystal.objects.get(id=crystal_id)
  return render(request, 'crystals/detail.html', { 'crystal': crystal })