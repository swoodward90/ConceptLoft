from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


from contest import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SecretProject.views.home', name='home'),
    # url(r'^SecretProject/', include('SecretProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'contest.views.home', name='home'),
    url(r'^business/$', 'contest.views.business', name='business'),
    url(r'^detail/(?P<contest_id>\d+)/$', 'contest.views.detail', name='detail'),
    url(r'^designers/$', 'contest.views.designers', name='designers'),
    url(r'^entry/(?P<contest_id>\d+)/$', 'contest.views.entry', name='entry'),
    url(r'^success/$', 'contest.views.success', name='success'),
    url(r'^entrysuccess/(?P<contest_id>\d+)/$', 'contest.views.entrysuccess', name='entrysuccess'),

)
if settings.DEBUG:
	# static files (images, css, javascript, etc.)
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))