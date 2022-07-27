from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Bar, Available
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import RatingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bars_index(request):
    bars = Bar.objects.all()
    return render(request, 'bars/index.html', { 'bars': bars })

def bars_detail(request, bar_id):
    bar = Bar.objects.get(id=bar_id)
    avaliable_bar_doesnt_have = Available.objects.exclude(id__in = bar.avaliable.all().values_list('id'))
    rating_form = RatingForm()
    return render(request, 'bars/detail.html', { 'bar': bar, 'rating_form': rating_form, 'avaliable': avaliable_bar_doesnt_have })

    
class BarCreate(CreateView):
    model = Bar
    fields = '__all__'
class BarUpdate(UpdateView):
    model = Bar
    fields = '__all__'
class BarDelete(DeleteView):
    model = Bar
    success_url = '/bars/'

def add_rating(request, bar_id):
	# create the ModelForm using the data in request.POST
  form = RatingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_rating = form.save(commit=False)
    new_rating.bar_id = bar_id
    new_rating.save()
  return redirect('detail', bar_id=bar_id)

class AvaliableList(ListView):
  model = Available

class AvailableDetail(DetailView):
  model = Available

class AvaliableCreate(CreateView):
  model = Available
  fields = '__all__'

class AvaliableUpdate(UpdateView):
  model = Available
  fields = ['name']

class AvaliableDelete(DeleteView):
  model = Available
  success_url = '/avaliable/'

def assoc_avaliable(request, bar_id, avaliable_id):
  Bar.objects.get(id=bar_id).avaliable.add(avaliable_id)
  return redirect('detail', bar_id=bar_id)