from django.db import models

# Create your models here.

class Usersignup(models.Model):
    firstname=models.CharField(max_length=20)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return str(self.firstname)

class Adminsignup(models.Model):
    name = models.CharField(max_length=50)
    staffid=models.CharField(max_length=50)
    # designation = model
    def __str__(self):
        return str(self.name)

class Room(models.Model):
    image = models.ImageField(upload_to='media/image/',default='')
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    capacity = models.IntegerField(blank=True,null=True)
    service = models.TextField(max_length=50)
    charges = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)


class Booking(models.Model):
    # location = models.CharField(max_length=20)
    check_in =models.DateField(max_length=20)
    check_out =models.DateField(max_length=20)
    adult = models.IntegerField(blank=True,null=True)
    child = models.IntegerField(blank=True,null=True)
    
    class Meta:
        get_latest_by = ['id']
    def __str__(self):
        return str(self.check_in)
