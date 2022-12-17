from django.db import models


class Event(models.Model):
    """
    Defines attributes of the event model
    """
    title = models.CharField(max_length=254)
    description = models.TextField()
    date = models.CharField(
        max_length=254, null=True, blank=True,
        help_text="Please use the following format: <em>DD-MM-YYYY</em>."),
    category = models.CharField(max_length=254),
    location = models.CharField(max_length=254, null=True, blank=True),
    user = models.CharField(max_length=24),
    people = models.IntegerField(null=True, blank=True),
    image = models.ImageField(null=True, blank=True),
    image_url = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.title
