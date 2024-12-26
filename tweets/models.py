from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.tweet.id}"


# 追加部分
def tweet_like(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if tweet.like_set.filter(user=request.user).exists():
        tweet.like_set.filter(user=request.user).delete()
        liked = False
    else:
        tweet.like_set.create(user=request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': tweet.like_set.count()})


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='retweets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} retweeted {self.original_tweet.id}"
