from datetime  import date
from django.db import models


PERIOD = [('DAY', 'Day'), ('WEEK', 'Week'), ('MONTH', 'Month'), ('QUARTER', 'Quarter'), ('YEAR', 'Year'),]
    
class Date(models.Model):
    ''' Date and period dimension '''
    date   = models.DateField(default=date.today, blank=True)
    period = models.CharField(max_length=16, choices=PERIOD, default="YEAR", null=True, blank=True)


class Account(models.Model):
    ''' General Ledger accounts OR derived (calculated) values '''
    name   = models.CharField(max_length=64, default="", null=True, blank=True)
    number = models.IntegerField(default=0)


class Corporation(models.Model):
    ''' Corporate name and ticker '''
    name   = models.CharField(max_length=64, default="", null=True, blank=True)
    ticker = models.CharField(max_length=5 , default="", null=True, blank=True)


class Value(models.Model):
    ''' Value fact table '''
    date        = models.ForeignKey(models.ForeignKey(Date,        on_delete=models.CASCADE, default="", null=True, blank=True, related_name='value'))
    account     = models.ForeignKey(models.ForeignKey(Account,     on_delete=models.CASCADE, default="", null=True, blank=True, related_name='value'))
    corporation = models.ForeignKey(models.ForeignKey(Corporation, on_delete=models.CASCADE, default="", null=True, blank=True, related_name='value'))
    value       = models.DecimalField(max_digits=12, decimal_places=2)
