import hashlib
import json
from django.utils import timezone

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views import generic
from mp3hash import mp3hash, TaggedFile

from Musicblock import settings
from Musicblock.settings import MEDIA_URL, SITE_URL
from .models import Music, Musicblock


#音樂列表
class MusicList(generic.ListView):
    model = Music
    template_name = "music_list.html"


# def hash(music_block: Dict[str, Any]) -> str:
#     """
#     生成块的 SHA-256 hash值
#     :param block: Block
#     """
#     block = {
#         'main_index': len(self.main_chain) + 1,
#         'timestamp': time(),
#         'proof': proof,
#         'music_hash': mp3hash(mp3path),
#         'previous_hash': previous_hash or self.hash(self.main_chain[-1]),
#     }
#     # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
#     music_block_string = json.dumps(music_block, sort_keys=True).encode()
#     return hashlib.sha256(music_block_string).hexdigest()



# def site(request):
#     return {'SITE_URL': settings.SITE_URL}
#

class MusicCreate(generic.CreateView):
    model = Music
    template_name = 'music_form.html'
    fields = ('musicname','singername','body','music')
#音樂新增的時候要建立一個音樂區塊(還沒寫)
    #新增音樂區塊並取得三枚音樂幣
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.music.name = str(timezone.now().strftime("%Y%m%d%H%M")) + "." + str(self.object.music.name.split(".")[-1])
        self.object.save()
        # self.object.music.open(mode='rb')
        # content = self.object.music.read()
        # hasher = hashlib.new('sha1')
        # maxbytes = None
        #
        # music_hash = TaggedFile(content).hash(maxbytes=maxbytes, hasher=hasher)
        # print(music_hash)
        # self.object.music.close()
        music_token = 00000
        musicblock = Musicblock.objects.create(music_hash=music_hash,music_token=music_token)

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


class MusicDetail(generic.DetailView):
    model = Music
    template_name = "music_detail.html"

    def get_object(self):
        return self.model.objects.filter(token=self.kwargs['token'])
