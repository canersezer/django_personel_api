from django.db import models
from django.contrib.auth.models import User


class Departman(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
    def count_person(self):
        return self.personel_set.count()
    
    
class Person(models.Model):

    title_choice=(  
        ("TL","Team Lead"),
        ("MD","Mid Lead"),
        ("JR","Junior"),
    )
    
    gender_choice=(
        ("M","Male"),
        ("F","Female"),
        ("O","Order"),
    )

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    title=models.CharField(choices=title_choice,max_length=10)
    gender=models.CharField(choices=gender_choice,max_length=10)
    salary = models.PositiveIntegerField()
    start_date = models.DateField(auto_now_add=True)
    departman = models.ForeignKey(Departman,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name