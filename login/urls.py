from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'logout.html'}, name='logout'),
    url(r'^home/$', views.home_view, name='account-redirect'),
    #url(r'^home/account/$', views.home_view, name='home_view')


]