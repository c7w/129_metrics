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


# Create your views here.


def index(req):
    
    now = datetime.date.today() + datetime.timedelta(days=1)
    
    
    countList = [1,2,3,4,50,6,7,8,9,10,11,12,13,155]
    props = {
        'year': 2021,
        'month': 10,
        'day': 30,
        'data': ','.join([str(d) for d in countList])
    }
    return render(req, 'index.html', props)