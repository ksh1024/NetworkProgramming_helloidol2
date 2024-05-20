from django.urls import path
from 하프라이프 import views

app_name = '하프라이프'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),

]