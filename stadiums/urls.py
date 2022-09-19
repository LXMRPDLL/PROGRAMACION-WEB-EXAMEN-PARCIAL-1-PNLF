from django.urls import path

from stadiums import views

app_name = 'stadiums'

urlpatterns = [
    path('', views.StadiumList.as_view(), name='stadium_list'),
    path('create/', views.StadiumCreate.as_view(), name='stadium_create'),
    path('<int:pk>/', views.StadiumDetail.as_view(), name='stadium_detail'),
    path('<int:pk>/update/', views.StadiumUpdate.as_view(), name='stadium_update'),
    path('<int:pk>/delete/', views.stadium_delete, name='stadium_delete'),
]