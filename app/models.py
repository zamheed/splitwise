from django.db import models


class Register(models.Model):
    cont = models.IntegerField(default=10, unique=True)
    email = models.EmailField(max_length=50, primary_key=True)
    name = models.CharField(max_length=20)
    psw = models.CharField(max_length=20)


class Expenditure(models.Model):
    email = models.ForeignKey(Register,on_delete=models.CASCADE)
    expense = models.CharField(max_length=20)
    date = models.DateField()
    cost = models.DecimalField(max_digits=5, decimal_places=1)
