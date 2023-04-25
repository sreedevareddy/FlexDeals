from django.db import models
from django.utils import timezone
# importing user model from django
from django.contrib.auth.models import User
from django.urls import reverse

# Post Model/class
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # one to many relationship b/w user and post using Foreignkey
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

