from django.db import models

class Employee(models.Model):
    class Gender(models.Choices):
        M = "M"
        F = "F"
        LGBT = "LGBT"
    first = models.CharField(max_length = 155)
    last = models.CharField(max_length = 155)
    gender = models.CharField(max_length = 10, choices = Gender.choices)
    birth = models.DateField()
    hire = models.DateField()
    salary = models.DecimalField(default = 0, max_digits = 10, decimal_places = 2)
    position = models.ForeignKey("employee.Position", on_delete = models.SET_NULL, null = True, blank = True)
    def fullname(self):
        return f"{self.first} {self.last}"

class EmployeeAddress(models.Model):
    employee = models.OneToOneField("employee.Employee", on_delete = models.PROTECT)
    location = models.TextField(null = True, blank = True)
    district = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 15)
    
class Department(models.Model):
    name = models.CharField(max_length = 155)
    manager = models.OneToOneField("employee.Employee", on_delete = models.SET_NULL, null = True, blank = True)
    
class Position(models.Model):
    name = models.CharField(max_length = 155)
    description = models.TextField(null = True, blank = True)
    department = models.ForeignKey("employee.Department", on_delete = models.SET_NULL, null = True, blank = True)

class Project(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank = True)
    manager = models.OneToOneField("employee.Employee", on_delete = models.SET_NULL, null = True, blank = True, related_name = "project_manager")
    due = models.DateField()
    start = models.DateField()
    staff = models.ManyToManyField("employee.Employee")
