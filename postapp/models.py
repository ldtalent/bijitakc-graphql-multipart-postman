from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    photo = models.FileField()
    caption = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self) -> str:
        return self.title
