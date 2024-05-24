from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,null=True,blank=False)
    body=models.TextField()
    image=models.ImageField(null=True,blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"pk":self.pk})

    @property
    def ImageURL(self):
        try:
            url=self.image.url
        except:
            url=""
        return url