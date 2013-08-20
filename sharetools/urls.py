from django.conf.urls import patterns, include, url
from app.views import home,tools
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sharetools.views.home', name='home'),
    # url(r'^sharetools/', include('sharetools.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^[/]?$',home.Index,name='index'),
    url(r'^(?P<name>.+?)\.html$',home.HtmlIndex,name='html.index'),
    url(r'^sitemap.txt$',home.Sitemap,name='sitemap'),

    url(r'^ifconfig[/]?$',tools.ifconfig,name='ifconfig'),
)
