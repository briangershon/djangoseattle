from django.contrib import admin
from twitsearch.models import Tweet, SearchResult

class TweetAdmin(admin.ModelAdmin):
        date_hierarchy = 'pub_time'
        list_display = ('user', 'pub_time', 'text')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(SearchResult)