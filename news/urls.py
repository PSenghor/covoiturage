from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^edit/(?P<news_id>\d+)/$', edit),
    (r'^delete/(?P<news_id>\d+)/$', delete),
    (r'^add$', add),
    (r'^show/(?P<news_id>\d+)/$',show),
    (r'^archives/', list_all),
	(r'^$', news_view),
)