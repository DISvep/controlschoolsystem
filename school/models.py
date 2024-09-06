from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')


class Class(models.Model):
    grade = models.IntegerField()
    letter = models.CharField(max_length=1)


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    in_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
