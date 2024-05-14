from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    role = models.CharField(max_length=50)

    class Meta:
        db_table = "person_table"
