from twitsearch.models import Tweet, SearchResult
from django.conf import settings
import django.utils.simplejson as json
from django.utils.encoding import smart_unicode

import httplib2, urllib
import datetime, time

def tweets(response):
    '''
    This is the context processor for tweets.
    
    Returns the context variable tweets to be used on all pages
    
    There can be a maximum 2.5 requests per minute (150 / hour), 
    we are going to limit this to two requests for updates per minute 
    '''
    try:
        result = SearchResult.objects.latest('search_datetime')
    except SearchResult.DoesNotExist:
        # This is for the first time loading the page
        result = SearchResult.objects.create(
                refresh_url = '',
                query = '',
                search_datetime = datetime.datetime.now(),
                max_id = 2839675552) # This is the first djangoseattle used
    half_a_minute = datetime.timedelta(seconds=30)
    if result.search_datetime + half_a_minute <= datetime.datetime.now():
        # We are past the half a minute delay we are 
        # instituting lets get some more twitter results
        # Create the http object
        http = httplib2.Http()
        # Our query options to the twitter api
        # For more info see: http://apiwiki.twitter.com/Twitter-Search-API-Method%3A-search
        query_options = {'q':'#djangoseattle',
                         'show_user':'True',
                         'rpp':'100',
                         'lang':'en',
                         'since_id':result.max_id
                         }
        # Get the response and the content
        # response has the standard http response objects
        # content has our json from twitter
        response, content = http.request(
            settings.TWITTER_SEARCH_URL + urllib.urlencode(query_options),
            'GET'
        )
        # Only proceed if we got a valid request
        # This means we will have some content in our json object
        if response['status'] == '200':
            # parse the returned data as json
            json_content = json.loads(content)
            # Create a new search result object
            new_result = SearchResult.objects.create(
                        refresh_url = json_content['refresh_url'],
                        query = json_content['query'],
                        search_datetime = datetime.datetime.now(),
                        max_id = json_content['max_id'])
            new_result.save()
            for result in json_content['results']:
                # turn the datetime that twitter gives us into something python likes
                pub_time = time.strptime(result['created_at'], "%a, %d %b %Y %H:%M:%S +0000")
                pub_time = datetime.datetime.fromtimestamp(time.mktime(pub_time))
                # create a new tweet object
                new_tweet = Tweet.objects.create(
                        pub_time = pub_time,
                        text = smart_unicode(result['text']),
                        user = result['from_user'],
                        result = new_result,
                        twitter_id = result['id'],
                        profile_image_url = result['profile_image_url']
                        )
                new_tweet.save()
    # only 10 tweets shown
    return {'tweets':Tweet.objects.all().order_by('-pub_time')[:10]}
