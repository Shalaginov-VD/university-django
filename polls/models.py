from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    def __str__(self):
        return self.group_name

class Student(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
