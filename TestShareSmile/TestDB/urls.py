from django.conf.urls import url
from TestDB import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^users/$', views.user_list.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail.as_view()),
    url(r'^usersInterface/$', views.UserList.as_view()),
    url(r'^usersInterface/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^causes/$', views.causes_list.as_view()),
    url(r'^causes/(?P<pk>[0-9]+)/$', views.causes_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
