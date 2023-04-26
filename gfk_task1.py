# IMPORT
import tweepy 
from django.shortcuts import render
from django.http import HttpResponse

# API
# Authentication for Twitter
key = "your_key"
secret = "your_secret"
access = "your_access_token"
access_secret = "your_access_secret"

# Set-up  API client
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, access_secret)
api = tweepy.API(auth)

#Only Results with Images
def result_images(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        only_images = request.POST.get('only_images', False)

        if only_images:
            search_query += ' filter:images'

        tweets = api.result_images(q=search_query)

        context = {
            'search_query': search_query,
            'only_images': only_images,
            'tweets': tweets
        }

        return render(request, 'result_images.html', context)

    return HttpResponse(status=405)
