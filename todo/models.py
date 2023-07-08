from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.
class ToDoListModel(models.Model):
    task = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    update_at = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.task

    class Meta:
        db_table = 'to_do_list'
