from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/glasnost/daily/$', 'api.views.glasnost_daily'),
    url(r'^api/glasnost/monthly/$', 'api.views.glasnost_monthly'),
    url(r'^api/glasnost/yearly/$', 'api.views.glasnost_yearly'),
)
