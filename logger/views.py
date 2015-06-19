from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,render
from django.http import JsonResponse

from rest_framework import viewsets

from logger.serializer import DeviceSerializer
from logger.form import DeviceForm
from logger.models import Device

import json

def get_data(request):
    '''Shall implement both get and post methods to collect data from loggers.
    Implement mine first  then try and use rest framework if time permits.
    This API will not be fully restful. Use restframework'''
    
    if request.method == "GET":
        date = request.GET.get("date",None)
        latitude = request.GET.get("latitude",None)
        longitude = request.GET.get("longitude",None)
        sensor_id = request.GET.get('sensorID',None)
        reading = request.GET.get('reading',None)
        
    elif request.method == "POST":
        date = request.GET.post("date",None)
        latitude = request.GET.post("latitude",None)
        longitude = request.GET.post("longitude",None)
        sensor_id = request.GET.post('sensorID',None)
        reading = request.GET.post('reading',None)
    else:
        return JSONResponse('could not fetch data')
        
@login_required
def index(request):
    ''' Shall handle main html page. Values can be input using this method'''    
    
    if request.method == "POST":
        date = request.POST.get("date",None)
        latitude = request.POST.get("latitude",None)
        longitude = request.POST.get("longitude",None)
        sensor_id = request.POST.get('sensor_id',None)
        reading = request.POST.get('reading',None)
                
        dev = Device.objects.create(
            date = date,
            latitude = latitude,
            longitude = longitude,
            sensor_id = sensor_id,
            reading = reading,
            )
        
        form = DeviceForm()
        dev_readings = Device.objects.all().values_list("reading",flat=True)
        
        args = {}
        args['form'] = form
        args['data'] = dev_readings
        args['success'] = "Reading taken and saved with id: " + str(dev.id)

        #return JsonResponse({"success":"Readings taken and saved with id: " + str(dev.id)})
        return render(request, 'index.html', args)
    else:
        form = DeviceForm()
        
        dev = Device.objects.all().values_list("reading",flat=True)
        
        args = {}
        args['form'] = form
        args['data'] = dev

    return render(request, 'index.html', args)
    #return render_to_response('index.html',{'form',form})


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
