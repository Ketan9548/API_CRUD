from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    esal = models.FloatField()


    def ___str___(self):
        return f"{self.eid}--{self.ename}"