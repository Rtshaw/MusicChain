from django.conf.urls import url

from myblock import views


urlpatterns = [
    # url(r'^qustion/create$', views.QuestionCreate.as_view(), name='question_create'),
    url(r'^music/list$', views.MusicList.as_view(), name='music_list'),
]
