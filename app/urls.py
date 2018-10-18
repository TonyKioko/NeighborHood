from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^new_nhood/$',views.new_nhood,name='add_neighborhood'),
    url(r'^new_business/$',views.new_business,name='add_business'),
    url(r'^alert/$',views.new_alert,name='new_alert'),





    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
