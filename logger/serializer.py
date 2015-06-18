from rest_framework import routers, serializers, viewsets

from logger.models import Device

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'date', 'longitude', 'latitude','sensor_id','reading')
