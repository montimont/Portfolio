from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='game_index'),
    path('<int:game_id>', views.detail, name='game_detail')
]
