from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from patients import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^temp_datas/', views.Temp_DataList.as_view()),
    url(r'^temp_datas/(?P<pk>[0-20]+)/', views.Temp_DataDetail.as_view()),
    url(r'^pulse_datas/', views.Pulse_DataList.as_view()),
    url(r'^pulse_datas/(?P<pk>[0-20]+)/', views.Pulse_DataDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)