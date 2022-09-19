from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import Stadium
from .forms import StadiumForm

# Create your views here.
class StadiumList(generic.View):
    template_name = 'stadiums/stadium-list.html'
    
    def get(self, request):
        queryset = Stadium.objects.filter(status=True)
        context = {
            'stadiums': queryset
        }
        return render(request, self.template_name, context)

class StadiumDetail(generic.View):
    template_name = 'stadiums/stadium-detail.html'
    
    def get(self, request, pk):
        queryset = Stadium.objects.get(pk=pk)
        context = {
            'stadium': queryset
        }
        return render(request, self.template_name, context)
    
class StadiumCreate(generic.CreateView):
    template_name = 'stadiums/stadium-create.html'
    model = Stadium
    form_class = StadiumForm
    success_url = reverse_lazy('stadiums:stadium_list')

class StadiumUpdate(generic.UpdateView):
    template_name = 'stadiums/stadium-update.html'
    model = Stadium
    form_class = StadiumForm
    success_url = reverse_lazy('stadiums:stadium_list')

def stadium_delete(request, pk):
    stadium = Stadium.objects.get(pk=pk, status=True)
    stadium.status = False
    stadium.save()
    return redirect('stadiums:stadium_list')