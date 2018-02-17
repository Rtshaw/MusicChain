from django.conf.urls import url

from user import views

urlpatterns = [
    # url(r'^qustion/create$', views.QuestionCreate.as_view(), name='question_create'),
    url(r'^user/(?P<token>[0-9a-f-]+)$', views.UserProfileDetail.as_view(), name='user_detail'),
    url(r'^user/(?P<token>[0-9a-f-]+)/update$', views.UserProfileUpdate.as_view(), name='user_update'),
    url(r'^sign-up$', views.SignUp.as_view(), name='sign-up'),

]
