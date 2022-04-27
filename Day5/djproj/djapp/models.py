from django.db import models

# Create your models here.

class Track(models.Model):
    track_name = models.CharField(max_length=20)
    def __str__(self):
        return self.track_name

class Student(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, default='Lname')
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)
    def __str__(self):
        return self.fname+" "+self.lname

    def is_adult(self):
        if self.age > 20:
            return True
        else:
            return False

    is_adult_short_description = "Adult"
    is_adult.boolean =True                 
