from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

  #  url(r'^$', views.signup, name='signup'),

#url(r'^$', core_views.home, name='home'),
 #   url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
  #  url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

    # url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home_view, name='account-redirect'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'logout.html'}, name='logout'),

]