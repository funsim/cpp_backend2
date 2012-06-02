from api.models import *
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from datetime import datetime, timedelta
from dateutil import parser

def glasnost_raw(request, model):
    kwargs = {}
    if 'start_date' in request.GET.keys():
        kwargs['rangedate__gte'] = request.GET['start_date']
    if 'end_date' in request.GET.keys():
        kwargs['rangedate__lte'] = request.GET['end_date']
    if 'source' in request.GET.keys():
        kwargs['source'] = request.GET['source']
    if 'destination' in request.GET.keys():
        kwargs['destination'] = request.GET['destination']

    objects = model.objects.using('mlab').filter(**kwargs)
    json = simplejson.dumps( [{'counter': o.counter,
                               'rangedate': o.rangedate,
                               'source': o.source,
                               'destination': o.destination} for o in objects], cls=DjangoJSONEncoder)
    return HttpResponse(json, mimetype='application/json')

def glasnost_daily(request):
    return glasnost_raw(request, GlasnostDaily)

def glasnost_monthly(request):
    return glasnost_raw(request, GlasnostMonthly)

def glasnost_yearly(request):
    return glasnost_raw(request, GlasnostYearly)

def glasnost_daily_mean(request, model = GlasnostDaily):
    ''' ''' 
    if not 'date' in request.GET.keys() or not 'data_points' in request.GET.keys() or not 'days_to_subtract' in request.GET.keys():
        return HttpResponse([], mimetype='application/json')

    date = parser.parse(request.GET['date'] + ' 00:00 UTC')

    objects = model.objects.using('mlab').filter(rangedate = date)
    objects_means = [] 
    for o in objects:
        mean = 0.0
        n = 0
        for i in range(int(request.GET['data_points'])):
            date = date - timedelta(days=int(request.GET['days_to_subtract']))
            try:
                mean += GlasnostDaily.objects.using('mlab').filter(rangedate = date, destination = o.destination, country_code = o.country_code)[0].counter
                n += 1
            except IndexError:
                pass
        if n > 0:
            mean /= n 
        objects_means.append(mean)

    json = simplejson.dumps( [{'mean': objects_means[i], 
                               'rangedate': objects[i].rangedate,
                               'source': objects[i].source,
                               'destination': objects[i].destination} for i in range(len(objects))], cls=DjangoJSONEncoder)
    return HttpResponse(json, mimetype='application/json')
