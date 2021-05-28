from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length=400)

    def __str__(self):
        return self.type

class Faculty(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=400)
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Student(models.Model):
    full_name = models.CharField(max_length=80)
    graduation_year = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
