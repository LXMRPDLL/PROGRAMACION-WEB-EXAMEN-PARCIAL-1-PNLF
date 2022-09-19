from django.urls import path

from players import views

app_name = 'players'

urlpatterns = [
    path('', views.PlayerList.as_view(), name='player_list'),
    path('create/', views.PlayerCreate.as_view(), name='player_create'),
    path('<int:pk>/', views.PlayerDetail.as_view(), name='player_detail'),
    path('<int:pk>/update/', views.PlayerUpdate.as_view(), name='player_update'),
    path('<int:pk>/delete/', views.player_delete, name='player_delete'),
]