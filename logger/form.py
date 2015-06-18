from django.forms import ModelForm
from logger.models import Device

class DeviceForm(ModelForm):
    class Meta:
        model  = Device
        fields = ['date','latitude','longitude','sensor_id','reading']

