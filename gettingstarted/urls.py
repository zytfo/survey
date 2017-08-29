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
    url(r'^en/survey', hello.views.survey, name='survey'),
    url(r'^ru/survey', hello.views.survey_ru, name='survey_ru'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^en/thanks', hello.views.thanks, name='thanks'),
    url(r'^ru/thanks', hello.views.thanks_ru, name='thanks_ru'),
    url(r'^en/results', hello.views.results, name='results'),
    url(r'^ru/results', hello.views.results_ru, name='results_ru'),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^auth/', hello.views.auth, name='auth')
 #   url(r'^logout/$', 'django.contrib.auth.views.logout')
]
