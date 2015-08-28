from django.db import models

# Create your models here.

# Simplified Event model
class Event(models.Model):
  calendarId = models.CharField(max_length=255),
  eventId = models.CharField(max_length=255),
  obtained = models.DateTimeField(auto_now_add=True),
