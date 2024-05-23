from django.shortcuts import render
from django.views.generic import ListView, DetailView

from 하프라이프.models import Character

class CharacterListView(ListView):
    model = Character #html파일로 모델이 들어감. Read
    # character_list = Character.objects.all() #DB에 모델 데이터 다 가져오자
    #return render(request, '하프라이프/character_list.html', context={'character_list': character_list})  # #모델_list.html에 모델_list라는 키로 DB에 가져온 데이터 넣어서 render하자

class CharacterDetailView(DetailView):
    model = Character
    # character = Character.objects.get(pk=pk)
    # return render(request, '하프라이프/character_detail.html' context={'character': character})