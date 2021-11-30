from datetime import datetime
import json
import Backend.settings as settings
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
import django.contrib.auth.models as AuthModels
from django.db.models import Q
from django.utils import timezone

from CodePlay.models.Game import Start, Result

# Create your views here.

def start(req):
    newStart = Start()
    newStart.save()
    return JsonResponse({'status': 'Accepted'})

def result(req):
    try:
        POST = json.loads(req.body)
        r = POST.get('result')
        li = [101,102,103,104,105]
        if r not in li:
            raise NotImplementedError
        newStart = Result(result=r)
        newStart.save()
        return JsonResponse({'status': 'Accepted'})
    except:
        return JsonResponse({'status': 'Runtime Error'})