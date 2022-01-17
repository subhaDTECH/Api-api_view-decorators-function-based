
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StduentSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST','PUT','PATCH',"DELETE"])
def student_api(request,pk=None):
    if request.method =="GET":
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StduentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StduentSerializer(stu,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=StduentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg':'data save '})
        return Response(serializer.errors)
    if request.method=="PUT":
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StduentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'meg':"data complete update"})
        return Response(serializer.errors)
    if request.method=="PATCH":
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StduentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'meg':"data partial update"})
        return Response(serializer.errors)
    if request.method=="DELETE":
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":"data delete success"})   




