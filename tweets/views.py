from django.shortcuts import render, redirect
from .forms import TweetForm
from django.contrib.auth.decorators import login_required

from .models import Tweet

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
