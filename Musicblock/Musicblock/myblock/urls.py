from django.conf.urls import url

from myblock import views

urlpatterns = [
    url(r'^music/create$', views.MusicCreate.as_view(), name='music_create'),
    url(r'^music/(?P<token>[0-9a-f-]+)$', views.MusicDetail.as_view(), name='music_detail'),
    url(r'^music/(?P<token>[0-9a-f-]+)/buy$', views.MusicBuy.as_view(), name='music_buy'),
    url(r'^music/(?P<token>[0-9a-f-]+)/listen', views.MusicListen.as_view(), name='music_listen'),
    url(r'^music/list$', views.MusicList.as_view(), name='music_list'),
    url(r'^$', views.MusicList.as_view(), name='index'),
]
