from django.shortcuts import render,get_object_or_404
from .models import ToDoListModel
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from .serializers import TodoSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerPermission

class ListToDoApiView(generics.ListCreateAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class DetailToDoApiView(generics.RetrieveAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class CreateToDoApiView(generics.CreateAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class DeleteToDoApiView(generics.RetrieveDestroyAPIView):
    queryset  = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class UpdatePatchApiView(generics.RetrieveUpdateAPIView):
    queryset  = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class UpdatePutApiView(generics.UpdateAPIView):
    queryset  = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class StatusUpdateView(APIView):
    def get(self,request,*args,**kwargs):
        task = get_object_or_404(ToDoListModel,pk=kwargs['task_id'])
        if task.status==False:
            task.status = True
            task.update_at = datetime.datetime.now()
            task.save()
            return Response({"message":"successfully update"})
        else:
            return Response({"message":"this task already done"})

class GetToDosByStatusView(APIView):
    def get(self,request,*args,**kwargs):
        status = True if kwargs['status_type'].title()=='True' else False
        all_todos = ToDoListModel.objects.filter(status=status)
        result = []
        for task in all_todos:
            result.append({
                "id":task.pk,
                "task":task.task,
                "status":task.status,
                "created_at":task.created_at,
                "update_at":task.update_at})
        return Response(result)
