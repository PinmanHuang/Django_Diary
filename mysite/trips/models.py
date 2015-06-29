from django.db import models

# Create your models here.
#欄位、資料型態
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
   	#新增現在的時間
    created_at = models.DateTimeField(auto_now_add=True)
    #terminal中可以回傳東西看到內容
    def __str__(self):
    	return self.title