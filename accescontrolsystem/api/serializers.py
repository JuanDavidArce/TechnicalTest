"""Api Serializers"""
# Python
from datetime import datetime
import pdb
import threading


# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token


# Models
from companies.models import AccesPoint, Schedule


# Utils
from utils.email import *


class ValidateAccessSerializer(serializers.Serializer):
    """Validate Acces serializer.
    Handle the validation for an access point"""
    acces_point_id = serializers.IntegerField()

    def validate(self,data):
        """Check credentials"""
        user = self.context['user']
        actual_time = datetime.now().time()
        actual_time = actual_time.replace(hour=actual_time.hour-5)
        acces_point = AccesPoint.objects.filter(pk = data['acces_point_id'])
        if not acces_point:
            raise serializers.ValidationError({'error':'Acces point does not exist'})
        schedules = Schedule.objects.filter(acces_point = acces_point[0],
                                            user = user).filter(start_time__lte = actual_time,
                                                                ending_time__gte = actual_time)
        if not schedules or not acces_point[0].is_active:
            thread = threading.Thread(target=send_user_mail, 
                                    args= (acces_point[0].company.administrator,'Unauthorized access attempt',
                                    'emails/unauthorized.html', 
                                    {'acces_point':acces_point,'operation':'unauthorized','user':user}, ))
            thread.start()
            raise serializers.ValidationError({'can access':False,'acces_point':AccessPointModelSerializer (acces_point[0]).data})
        
        return data

    def create(self,data):
        """Retrieve acces point"""
        acces_point = AccesPoint.objects.get(pk = data['acces_point_id'])
        return acces_point


class AccessPointModelSerializer(serializers.ModelSerializer):
    """ArccesPoint model serializer"""

    class Meta:
        """Meta class"""
        model= AccesPoint
        fields = '__all__'
