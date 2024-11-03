from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name