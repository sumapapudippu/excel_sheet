from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^blog/',views.post_list_view),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    	views.post_detail_view, name = 'post_detail'), #name is canonical form
    url(r'^(?P<id>\d+)/share/$', views.mail_send_view,name = 'sendmail')
]