from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from employee_api.serializers import EmployeeSerializer
from .models import Employee



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ["first_name", "last_name"]
    filterset_fields = ['last_name', 'birth_date']
    ordering_fields = ["last_name"]
