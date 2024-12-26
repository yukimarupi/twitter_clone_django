from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
]
urlpatterns += [
    path('<int:tweet_id>/like/', views.tweet_like, name='tweet_like'),
]

urlpatterns += [
    path('register/', views.register, name='register'),
]

urlpatterns += [
    path('<int:user_id>/follow/', views.follow_user, name='follow_user'),
]
urlpatterns += [
    path('<int:tweet_id>/retweet/', views.retweet, name='retweet'),
]
