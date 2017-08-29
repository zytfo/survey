from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^survey', hello.views.survey, name='survey'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thanks', hello.views.thanks, name='thanks'),
    url(r'^results', hello.views.results, name='results'),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^auth/', hello.views.auth, name='auth'),
    url(r'^changelang/', hello.views.changelang, name='auth')
 #   url(r'^logout/$', 'django.contrib.auth.views.logout')
]
