# Create your models here.
from django.db import models

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    busno = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name

class User(models.Model):
    CHOICES = (
        ('Elite', (
            ('AC sleeper','AC sleeper'),
            ('Non-AC sleeper','Non-AC sleeper'),
            ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
            ('AC seater','AC seater'),
        )),
        ('Premium', (
            ('Non-AC sleeper','Non-AC sleeper'),
            ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
            ('AC seater','AC seater'),
        )),
        ('Normal', (
            ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
            ('AC seater','AC seater'),
        )),
    )
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    category = models.CharField(max_length=30,choices=CHOICES)

    def __str__(self):
        return self.email

class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid = models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email


