from django.urls import path,include
from . import views
urlpatterns = [
    path('dashboard',views.index),
    path('feed',views.feed),
    path('add-new-bug',views.newbug),
    path('my-post/<int:id>',views.postie),
    path('my-post/feedback',views.feedback),
    path('leaderboard',views.leaderboard),
]
