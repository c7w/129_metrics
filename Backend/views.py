import time
import math
import datetime
from django import db
from django.db import models
import Backend.settings as settings
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
import django.contrib.auth.models as AuthModels
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.db.models import Q
from django.utils import timezone

from CodePlay.models.Game import Start, Result


# Create your views here.


def index(req):
    
    now = datetime.date.today() + datetime.timedelta(days=1)
    countList = []
    
    for i in range(0, 21):
        countList.append(Start.objects.filter(time__lte = now-datetime.timedelta(days=i)).count())
    countList = list(reversed(countList))
    
    three_week_ago = datetime.date.today() - datetime.timedelta(days=20)
    
    data2 = []
    for i in range(101, 106):
        data2.append(Result.objects.filter(result=i).count())
    props = {
        'year': three_week_ago.year,
        'month': three_week_ago.month-1,
        'day': three_week_ago.day,
        'data': ','.join([str(d) for d in countList]),
        'data2': data2
    }
    return render(req, 'index.html', props)