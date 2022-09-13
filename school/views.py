from this import s
from django.http.response import JsonResponse
from django.shortcuts import render,get_object_or_404
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class CBV_List(APIView):
    def get(self, request):
        students=student.objects.all()
        serializer=studentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def post(self,request):
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
          
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class CBV_List1(APIView):
    def get(self,request,pk):
        students=get_object_or_404(student,pk=pk)
        serializer=studentSerializer(students)
        return Response(serializer.data)

    def put(self,request,pk):
        students=get_object_or_404(student,pk=pk)
        serializer=studentSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        students=get_object_or_404(student,pk=pk)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#=================================================================
#mixin     which make code easy          the way for easy code 

class mixin_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)

#===================================================================

#generics

class generic_list(generics.ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer


class generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer


#====================================================================
#viewset

class viewsets_subject(viewsets.ModelViewSet):
    queryset=subject.objects.all()
    serializer_class=subjectSerializer
    authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]


class viewsets_teacher(viewsets.ModelViewSet):
    queryset=teacher.objects.all()
    serializer_class=teacherSerializer


class viewsets_student(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studentSerializer