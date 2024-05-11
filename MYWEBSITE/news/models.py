from django.db import models
from tinymce.models import HTMLField
class News(models.Model):
  news_title = models.CharField(max_length=100)
  news_desc = HTMLField()
  news_image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)
# Create your models here.
