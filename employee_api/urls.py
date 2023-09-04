from django.urls import path
from django.urls import include, path
from rest_framework import routers
from employee_api import views


router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
