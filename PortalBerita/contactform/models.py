from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    txt = models.TextField()
    date = models.DateField(auto_now_add=True)  # Tanggal otomatis saat data dibuat
    time = models.TimeField(auto_now_add=True)  # Waktu otomatis saat data dibuat

    def __str__(self):
        return self.name