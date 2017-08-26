from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^survey$', hello.views.survey, name='survey'),
    url(r'^survey_ru', hello.views.survey_ru, name='survey_ru'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thanks', hello.views.thanks, name='thanks'),
    url(r'^thanks_ru', hello.views.thanks_ru, name='thanks_ru'),
    url(r'^results', hello.views.results, name='results'),
]
