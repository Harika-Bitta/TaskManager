from django.db import models

# Create your models here.
#creating two tables(department,task)
class Department(models.Model):
    # Objects = None
    department=models.CharField(max_length=100)

    # returning string
    # below lines for , change the display name in our Django model. The __str__() function in the Django model
    # returns a string that is the same as the display name of the instances of the model.
    def  __str__(self):
        return self.department

class Task(models.Model):
    task_created=models.DateField()
    name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    task=models.TextField(max_length=500)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.name
 # above lines for , change the display name in our Django model. The __str__() function in the Django model
 # returns a string that is the same as the display name of the instances of the model.





