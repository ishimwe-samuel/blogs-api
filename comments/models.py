from django.db import models

# Create your models here.
class Comment(models.Model):
    comment=models.CharField( max_length=50)    
    blog=models.ForeignKey("blog.Blog", verbose_name=_(""), on_delete=models.CASCADE)