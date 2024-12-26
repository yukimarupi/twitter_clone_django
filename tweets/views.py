from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from tweets.forms import TweetForm  # DjangoのUserモデル
from .models import Retweet, Tweet, Follow  # TweetとFollowモデル

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # 最新順
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # ログインユーザーを投稿者として設定
            tweet.save()
            return redirect('tweet_list')  # ツイート一覧にリダイレクト
    else:
        form = TweetForm()
    return render(request, 'tweets/tweet_create.html', {'form': form})

@login_required
def tweet_like(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if tweet.like_set.filter(user=request.user).exists():
        tweet.like_set.filter(user=request.user).delete()
        liked = False
    else:
        tweet.like_set.create(user=request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': tweet.like_set.count()})

@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    if request.user.following.filter(following=user_to_follow).exists():
        request.user.following.filter(following=user_to_follow).delete()
        following = False
    else:
        Follow.objects.create(follower=request.user, following=user_to_follow)
        following = True
    return JsonResponse({'following': following})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 登録後にログインページへリダイレクト
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def retweet(request, tweet_id):
    original_tweet = Tweet.objects.get(id=tweet_id)
    Retweet.objects.create(user=request.user, original_tweet=original_tweet)
    return JsonResponse({'message': 'Retweeted successfully!'})
def retweet(request, tweet_id):
    original_tweet = get_object_or_404(Tweet, id=tweet_id)  # ツイートが存在しない場合は404エラーを返す
    # リツイートが既に存在するか確認
    if Retweet.objects.filter(user=request.user, original_tweet=original_tweet).exists():
        return JsonResponse({'message': 'You already retweeted this post!'}, status=400)
    # リツイートを作成
    Retweet.objects.create(user=request.user, original_tweet=original_tweet)
    return JsonResponse({'message': 'Retweeted successfully!'})