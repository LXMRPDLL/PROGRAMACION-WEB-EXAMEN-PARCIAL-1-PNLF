from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Team
from players.models import Player
from .forms import TeamForm

# Create your views here.
class TeamList(generic.View):
    template_name = 'teams/team-list.html'
    
    def get(self, request):
        queryset = Team.objects.filter(status=True)
        context = {
            'teams': queryset
        }
        return render(request, self.template_name, context)

class TeamDetail(generic.View):
    template_name = 'teams/team-detail.html'
    
    def get(self, request, pk):
        queryset = Team.objects.get(pk=pk)
        context = {
            'team': queryset
        }
        return render(request, self.template_name, context)

class TeamCreate(generic.CreateView, SuccessMessageMixin):
    template_name = 'teams/team-create.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams:team_list')

    def get_success_message(self, cleaned_data):
        return "Team Created Successfully"

class TeamUpdate(generic.UpdateView, SuccessMessageMixin):
    template_name = 'teams/team-update.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams:team_list')

    def get_success_message(self, cleaned_data):
        return "Team Updated Successfully"

class TeamDelete(generic.DeleteView):
    template_name = 'teams/team-delete.html'
    model = Team
    success_url = reverse_lazy('teams:team_list')

def team_delete(request, pk):
    team = Team.objects.get(pk=pk, status=True)
    team.status = False
    team.save()
    messages.success(request, 'Team Deleted Successfully')
    return redirect('teams:team_list')