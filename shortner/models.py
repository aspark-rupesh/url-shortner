from django.db import models

from user.models import User

# Create your models here.

class ShortUrl(models.Model):
    original_url = models.URLField()
    short_key = models.CharField(max_length=20)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="short_urls")
    qr_code = models.FileField(upload_to="qr_codes/",blank=True,null=True)
    hit_count = models.IntegerField(default=0)
    custom_key = models.CharField(max_length=20,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True,null=True)




    

# class UrlInfo(models.Models):
#     url = models.OneToOneField(ShortUrl,on_delete=models.CASCADE,related_name="info")
