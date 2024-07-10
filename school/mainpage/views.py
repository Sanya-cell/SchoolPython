from django.shortcuts import render, get_object_or_404, redirect
from mainpage.models import Article, Class, Schedule, Student, Journal, Lesson
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json
from itertools import groupby
from django.contrib.auth import authenticate, login, logout
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart





def schedule(request):
    if not request.user.is_authenticated:
        return redirect("/")
    classes = Class.objects.all()
    sched = Schedule.objects.all()
    return render(request, 'schedule.html', {'classes': classes, 'schedule': sched})


def news(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'news.html', context)


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id) #Получаем статью или 404 ошибку
    return render(request, 'article.html', {'article': article})





