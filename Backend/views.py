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
    props = {}
    return render(req, 'index.html', props)