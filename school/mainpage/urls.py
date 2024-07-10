from django.urls import path, re_path, include
from mainpage import views


urlpatterns = [
    path('', views.news, name='news'),
    path('article/<int:article_id>/', views.show_article, name='article'),
    path('schedule/', views.schedule, name='schedule'),
]
