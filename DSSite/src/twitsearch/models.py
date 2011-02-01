from django.db import models
from django.conf import settings

# Micah Ransdell 07-25-2009
# Django Sprint
# Models taken from Django-Syncr

class BigIntegerField(models.IntegerField):
    """
    Defines a PostgreSQL compatible IntegerField needed to prevent 'integer 
    out of range' with large numbers.
    """
    def get_internal_type(self):
        return 'BigIntegerField'

    def db_type(self):
        if settings.DATABASE_ENGINE == 'oracle':
            db_type = 'NUMBER(19)'
        else:
            db_type = 'bigint'
        return db_type
    
    
class SearchResult(models.Model):
    '''
    Search results from the twitter search api
    '''
    refresh_url = models.CharField(blank=True, max_length=500)
    query = models.CharField(blank=True, max_length=250)
    max_id = BigIntegerField(blank=True)
    search_datetime = models.DateTimeField()
    
    def __unicode__(self):
        return u'%s %s' % (self.query, unicode(self.search_datetime))
    
    def results(self):
        return self.tweet_set.all()
    
    
class Tweet(models.Model):
    pub_time = models.DateTimeField()
    twitter_id = BigIntegerField(unique=True)
    text = models.TextField()
    user = models.CharField(blank=True, max_length=15)
    result = models.ForeignKey(SearchResult, default=1)
    profile_image_url = models.URLField(verify_exists=False, max_length=300)

    def __unicode__(self):
        return u'%s %s' % (self.user, self.pub_time)

    def url(self):
        return u'http://twitter.com/%s/statuses/%s' % (self.user, self.twitter_id)

    def local_pub_time(self):
        '''
        Convert the Twitter timestamp stored in pub_time to the timezone
        specified in DJANGO_SETTINGS_MODULE. Requires pytz.
        '''
        import pytz
        zone = pytz.timezone(settings.TIME_ZONE)
        return self.pub_time.replace(tzinfo=pytz.utc).astimezone(zone)
