from django.urls import path
from .views import EmployeeDetail,EmployeeInfo


urlpatterns = [
    path("emp/",EmployeeDetail.as_view(),name="emp"),
    path("empinfo/<int:id>",EmployeeInfo.as_view(),name="empinfo"),
]
