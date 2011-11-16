from django.contrib import admin
from bookmarks.models import *

class LinkAdmin(admin.ModelAdmin):
	pass

class BookmarkAdmin(admin.ModelAdmin):
	list_display=('title','link','user',)
	list_filter =('user',)
	ordering = ('title',)
	search_fields =('title',)

class TagAdmin(admin.ModelAdmin):
	pass

class SharedbookmarkAdmin(admin.ModelAdmin):
	list_display = ('bookmark',)

	
admin.site.register(Link,LinkAdmin)
admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(SharedBookmark,SharedbookmarkAdmin)

