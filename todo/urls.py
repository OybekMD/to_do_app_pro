from django.urls import path
from .views import (ListToDoApiView,DetailToDoApiView,CreateToDoApiView,
                    DeleteToDoApiView,UpdatePatchApiView,UpdatePutApiView,
                    StatusUpdateView,GetToDosByStatusView)

urlpatterns = [
    path('',ListToDoApiView.as_view()),
    path('<pk>/',DetailToDoApiView.as_view()),
    # path('create/',CreateToDoApiView.as_view()),
    # path('delete/<int:task_id>/',DeleteToDoApiView.as_view()),
    # path('update_patch/<int:task_id>/',UpdatePatchApiView.as_view()),
    # path('update_put/<int:task_id>/',UpdatePutApiView.as_view()),
    # path('status/<int:task_id>/',StatusUpdateView.as_view()),

    # path('done/<str:status_type>/',GetToDosByStatusView.as_view()),
]