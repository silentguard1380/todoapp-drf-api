from django.db import models

# Create your models here.


class Todo(models.Model):

    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    class Meta:
        db_table = "todos"   # نامی که جدولمان در دیتابیس ذخیره میشود