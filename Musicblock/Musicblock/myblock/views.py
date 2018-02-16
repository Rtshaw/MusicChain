from django.shortcuts import render

from django.views import generic

from .models import Music

#音樂列表
class MusicList(generic.ListView):
    model = Music
    template_name = "music_list.html"
