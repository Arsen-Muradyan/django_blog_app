from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now)
  def __str__(self):
    return format(self.title)