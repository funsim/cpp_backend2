from api.models import *
from django.core import serializers
from django.http import HttpResponse

def glasnost_daily(request):
    result = GlasnostDaily.objects.using('mlab').all()
    output = serializers.serialize("json", result)
    return HttpResponse(output, mimetype='application/json')

def glasnost_yearly(request):
    kwargs = {}
    if 'start_date' in request.GET.keys():
        kwargs['date__gte'] = request.GET['start_date']
    if 'end_date' in request.GET.keys():
        kwargs['date__lte'] = request.GET['end_date']
    if 'source' in request.GET.keys():
        kwargs['source'] = request.GET['source']
    if 'destination' in request.GET.keys():
        kwargs['destination'] = request.GET['destination']

    result = GlasnostYearly.objects.using('mlab').filter(**kwargs)
    output = serializers.serialize("json", result)
    return HttpResponse(output, mimetype='application/json')
