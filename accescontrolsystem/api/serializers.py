"""Api Serializers"""
# Python
from datetime import datetime


# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Models
from companies.models import AccesPoint, Schedule


class ValidateAccessSerializer(serializers.Serializer):
    """Validate Acces serializer.
    Handle the validation for an access point"""

    acces_point_id = serializers.IntegerField()
    time = serializers.TimeField(default= datetime.now())
    read_only_fields = ['time']


    def validate(self,data):
        """Check credentials"""
        user = self.context['user']
        acces_point = AccesPoint.objects.filter(pk = data['acces_point_id'])
        if not acces_point:
            raise serializers.ValidationError({'error':'Acces point does not exist'})
        schedules = Schedule.objects.filter(acces_point = acces_point[0],
                                            user = user).filter(start_time__gte = data['time'],
                                                                ending_time__lte = data['time'])
        if not schedules:
            raise serializers.ValidationError({'error':'You are not allowed to enter, the administrator will be notified'})
        
        return data


    def create(self,data):
        """Retrieve acces point"""
        acces_point = AccesPoint.objects.get(pk = data['acces_point_id'])
        return acces_point


class AccessPointModelSerializer(serializers.ModelSerializer):
    """Circle model serializer"""

    class Meta:
        """Meta class"""
        model= AccesPoint
        fields = '__all__'
