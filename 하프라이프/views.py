from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from 하프라이프.models import Character

class CharacterListView(ListView):
    model = Character #html파일로 모델이 들어감. Read
    # character_list = Character.objects.all() #DB에 모델 데이터 다 가져오자
    #return render(request, '하프라이프/character_list.html', context={'character_list': character_list})  # #모델_list.html에 모델_list라는 키로 DB에 가져온 데이터 넣어서 render하자

class CharacterDetailView(DetailView):
    model = Character
    # character = Character.objects.get(pk=pk)
    # return render(request, '하프라이프/character_detail.html' context={'character': character})

class CharacterCreateView(CreateView):
    model = Character
    fields = ['name','feature', 'photo']      #'__all__'
    template_name_suffix = '_create' #character_form.html -> character_create.html
    success_url = reverse_lazy('하프라이프:character_list') #만들기 성공할 때 이동할 URL
    
class CharacterUpdateView(UpdateView):
    model = Character
    fields = '__all__' #['name', 'feature', 'photo']
    template_name_suffix = '_update' # character_form.html에서 character_update.html로 고쳐줌
    success_url = reverse_lazy('하프라이프:character_list') #수정 성공시 이동할 URL

class CharacterDeleteView(DeleteView):
    model = Character
    success_url = reverse_lazy('하프라이프:character_list') #삭제 성공시 이동할 URL