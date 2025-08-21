from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250) 
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='records')
    phone = models.IntegerField()
    tall = models.IntegerField()
    weight = models.IntegerField()
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
