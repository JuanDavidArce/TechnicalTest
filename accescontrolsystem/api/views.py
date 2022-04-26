# Rest framework
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


# Models
from users.models import User


# Permissions
from rest_framework.permissions import IsAuthenticated


# Serializers
from api.serializers import ValidateAccessSerializer,AccessPointModelSerializer


class ApiAccessControlViewSet(GenericViewSet):
    """APi view set.
    
    Handle verification access
    """
    queryset = User.objects.filter(is_active = True)

    def get_permissions(self):
        """Assign permissions based on action"""
        if self.action in ['validate_access']:
            permissions = [IsAuthenticated()]
        return permissions


    @action(methods = ["POST"],detail = False)
    def validate_access(self,request):
        """Validates that a user is authorized to enter a company"""
        user = request.user
        serializer = ValidateAccessSerializer(data = request.data,context ={'user':user} )
        serializer.is_valid(raise_exception=True)
        acces_point =  AccessPointModelSerializer(serializer.save()).data
        return Response(data = acces_point, status = status.HTTP_200_OK)