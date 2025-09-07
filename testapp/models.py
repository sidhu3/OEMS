from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class role(models.Model):
    name =models.CharField(max_length=100, null=False)  

    def __str__(self):
        return self.name  

class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name= models.CharField(max_length=100) 
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    role = models.ForeignKey(role,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s " %(self.first_name,self.last_name,self.phone) 
    
    def get_absolute_url(self):
        return "/all_emp"
    


    