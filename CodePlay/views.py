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
        newStart = Result(result=req.POST.get('result'))
        newStart.save()
        return JsonResponse({'status': 'Accepted'})
    except:
        return JsonResponse({'status': 'Runtime Error'})