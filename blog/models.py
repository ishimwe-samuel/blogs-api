from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Blog(models.Model):
    owner=models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    title=models.CharField( max_length=50)  
    content=models.TextField()
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title