from ast import arg
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import New
from .forms import NewForm

# Create your views here.
class NewListView(ListView):
    model = New

class NewDetailView(DetailView):
    model = New
    
class NewCreate(CreateView):
    model = New
    form_class = NewForm
    success_url = reverse_lazy('news:news')
    
class NewUpdate(UpdateView):
    model = New
    form_class = NewForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('news:update', args=[self.object.id]) + '?ok'
    
class NewDelete(DeleteView):
    model = New
    success_url = reverse_lazy('news:news')