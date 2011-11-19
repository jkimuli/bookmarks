from django.conf.urls.defaults import patterns, include, url
from bookmarks.views import main_page,logout_page,register_page,bookmark_save_page,tag_page,ajax_tag_autocomplete
import os
from django.views.generic.simple import direct_to_template
from bookmarks.views import bookmark_vote_page,popular_page,friends_page,friend_add
from bookmarks.feeds import *

site_media = os.path.join(os.path.dirname(__file__),'site_media')


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {
	'recent': RecentBookmarks,
	'user': UserBookmarks
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #Browsing
    url(r'^$',main_page),
    url(r'^user/(\w+)/$','bookmarks.views.user_page'),
    
    #Session Management
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$',logout_page),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':site_media}),
    url(r'^register/$',register_page),
    url(r'^register/success/$',direct_to_template,{'template':'registration/register_success.html'}),
    
    #Account Management
    url(r'^save/$',bookmark_save_page),
    url(r'^tag/([^\s]+)/$', tag_page),
    url(r'^tag/$','bookmarks.views.tag_cloud_page'),
    url(r'^search/$','bookmarks.views.search_page'),
    
    #Ajax
    
    url(r'^ajax/tag/autocomplete/$',ajax_tag_autocomplete),
    
    url(r'^vote/$',bookmark_vote_page),
    url(r'^popular/$',popular_page),
    url(r'^comments/',include('django.contrib.comments.urls')),
    url(r'^bookmark/(\d+)/$','bookmarks.views.bookmark_page'),
    
    #Feeds
    url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds}),
    
    #Social
    
    url(r'^friends/(\w+)/$',friends_page),
    url(r'^friend/add/$',friend_add),

)
