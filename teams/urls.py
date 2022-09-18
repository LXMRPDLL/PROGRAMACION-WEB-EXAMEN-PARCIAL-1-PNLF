from django.urls import path

from teams import views

app_name = 'teams'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.TeamList.as_view(), name='team_list'),
    path('<int:pk>/', views.TeamDetail.as_view(), name='team_detail'),
    path('create/', views.TeamCreate.as_view(), name='team_create'),
    path('<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
    path('<int:pk>/delete/', views.team_delete, name='team_delete'),
]