from django.conf.urls import url 
from . import views 


urlpatterns = [
    url('^$', views.welcome, name = 'welcome'),  #url to direct to the home page
    url('^today/$', views.todays_pics, name = 'todaysPics'),  #url to direct to pictures posted today
]