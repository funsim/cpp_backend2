from api.models import *
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

def glasnost_result(request, model):
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
    return glasnost_result(request, GlasnostDaily)

def glasnost_monthly(request):
    return glasnost_result(request, GlasnostMonthly)

def glasnost_yearly(request):
    return glasnost_result(request, GlasnostYearly)
