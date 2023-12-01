from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField()
    salary = models.TextField()

    def __str__(self):
        return self.name