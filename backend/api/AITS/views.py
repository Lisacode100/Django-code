from rest_framework import viewsets
from .serializers import CustomUserSerializer, DepartmentSerializer, CourseUnitSerializer, ProgramSerializer, IssueSerializer
from .models import CustomUser, Department, CourseUnit, Program, Issue


# Create your views here.

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class DepartmentViewset(viewsets.ModelViewSet):
    queryset= Department.objects.all()  
    serializer_class=DepartmentSerializer

class CourseUnitViewset(viewsets.ModelViewSet):
    queryset=CourseUnit.objects.all()
    serializer_class= CourseUnitSerializer

class ProgramViewset(viewsets.ModelViewSet):
    queryset= Program.objects.all()
    serializer_class= ProgramSerializer

class IssueViewset(viewsets.ModelViewSet):
    queryset= Issue.objects.all()
    serializer_class= IssueSerializer


 

