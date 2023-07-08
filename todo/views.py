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
    queryset  = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class CreateToDoApiView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            print(request.data)
            queryset = ToDoListModel()
            queryset.task = request.data['task']
            queryset.save()
        except:
            return Response({"message":"please enter task"},400)
        return Response({'message':'object successfully created'},201)

class DeleteToDoApiView(APIView):
    def delete(self,request,*args,**kwargs):
        task = get_object_or_404(ToDoListModel,pk=kwargs['task_id'])
        task.delete()
        return Response({'message':'object successfully deleted'})

class UpdatePatchApiView(APIView):
    def patch(self,request,*args,**kwargs):
        task = get_object_or_404(ToDoListModel,pk=kwargs['task_id'])
        if 'task' in request.data:
            task.task = request.data['task']
            task.save()
        return Response({"message":"success"})

class UpdatePutApiView(APIView):
    def put(self,request,*args,**kwargs):
        task = get_object_or_404(ToDoListModel,pk=kwargs['task_id'])
        try:
            task.task = request.data['task']
            task.status = request.data['status']
            task.created_at = request.data['created_at']
            task.update_at = request.data['update_at']
            task.save()
        except KeyError:
            return Response({'message':'please private task, status, created_at and update_at'},400)
        except RuntimeError:
            return Response({"message":"Not Found"},500)
        return Response({"message":"seccessfully update"})

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
