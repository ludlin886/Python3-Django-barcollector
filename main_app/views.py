from django.shortcuts import render
from django.http import HttpResponse
from .models import Bar
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return HttpResponse('<h1>What''s Poping this is home page</h1>')

def about(request):
    return render(request, 'about.html')

def bars_index(request):
    bars = Bar.objects.all()
    return render(request, 'bars/index.html', { 'bars': bars })

def bars_detail(request, bar_id):
    bar = Bar.objects.get(id=bar_id)
    return render(request, 'bars/detail.html', { 'bar': bar })

class BarCreate(CreateView):
    model = Bar
    fields = '__all__'
class BarUpdate(UpdateView):
    model = Bar
    fields = ['description', 'price']
class BarDelete(DeleteView):
    model = Bar
    success_url = '/bars/'
