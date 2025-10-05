from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    """
    Blog Post model.

    Fields:
    - title: short title of the post
    - content: full text of the post
    - published_date: auto timestamp when created
    - author: reference to the user who created the post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # used by CreateView/UpdateView to redirect after saving
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
