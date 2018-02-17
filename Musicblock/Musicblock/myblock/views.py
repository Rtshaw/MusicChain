from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views import generic

from .models import Music

#音樂列表
class MusicList(generic.ListView):
    model = Music
    template_name = "music_list.html"


class MusicCreate(generic.CreateView):
    model = Music
    template_name = 'music_form.html'
    fields = ('musicname','singername','body','music')
#音樂新增的時候要建立一個音樂區塊(還沒寫)
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, '音樂已新增')
        return reverse('index')

# def homepage(request):
#     return render(request, 'homepage.html')


#新增交易(sender、recipient、amount)


# /transactions/new 创建一个交易并添加到区块
# /mine 告诉服务器去挖掘新的区块
# /chain 返回整个区块链


