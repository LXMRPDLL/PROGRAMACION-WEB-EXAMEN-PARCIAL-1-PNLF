from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Player
from teams.models import Team
from .forms import PlayerForm

# Create your views here.
class PlayerList(generic.View):
    template_name = 'players/player-list.html'

    def get(self, request):
        queryset = Player.objects.filter(status=True)
        context = {
            'players': queryset
        }
        return render(request, self.template_name, context)

class PlayerDetail(generic.View):
    template_name = 'players/player-detail.html'

    def get(self, request, pk):
        queryset = Player.objects.get(pk=pk)
        context = {
            'player': queryset
        }
        return render(request, self.template_name, context)

class PlayerCreate(generic.CreateView, SuccessMessageMixin):
    template_name = 'players/player-create.html'
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('players:player_list')

    def get_success_message(self, cleaned_data):
        return "Player Created Successfully"

class PlayerUpdate(generic.UpdateView, SuccessMessageMixin):
    template_name = 'players/player-update.html'
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('players:player_list')

    def get_success_message(self, cleaned_data):
        return "Player Updated Successfully"

def player_delete(request, pk):
    player = Player.objects.get(pk=pk, status=True)
    player.status = False
    player.save()
    messages.success(request, 'Player Deleted Successfully')
    return redirect('players:player_list')