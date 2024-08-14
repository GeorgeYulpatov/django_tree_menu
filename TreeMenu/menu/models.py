from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Menu Name")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    url = models.CharField(max_length=200, blank=True, verbose_name="URL")
    named_url = models.CharField(max_length=200, blank=True, verbose_name="Named URL")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url
