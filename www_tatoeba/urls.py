from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^www_tatoeba/', include('www_tatoeba.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # Tatoeba url
	(r'^\w+/?$', 'views.index.index'),
	(r'^\w+/users/check_login/?$', 'views.users.check_login'),
	(r'^\w+/users/logout/?$', 'views.users.logout'),
    (r'^\w+/sentences/show/(?P<sentence_id>\d+)/?$', 'views.sentences.show'),
)
