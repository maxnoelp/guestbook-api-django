from django.db import models

# Create your models here.
class guestBook(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=700)
    date = models.DateField()
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name