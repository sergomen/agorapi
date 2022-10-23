from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField
from url_or_relative_url_field.fields import URLOrRelativeURLField

# Create your models here.


def get_default_links():
    return {"youtube":"youtube.com/username",
         "twitter":"twitter.com/username",
         "github":"github.com/username"}

class Advocate(models.Model):
    profile_pic = models.ImageField(upload_to='avatar/', default='/avatar/default.png', blank=True)
    # username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="username", null=True)
    username = models.CharField(max_length=30, unique=True, null=True)
    name = models.CharField(max_length=256, default='')
    short_bio = models.CharField(max_length=500, default='')
    long_bio = models.TextField(default='')
    advocate_years_exp = models.PositiveIntegerField(null=True)
    company = models.ManyToManyField('Company', blank=True, related_name="companies")
    link = JSONField(null=False, blank=True, default=dict)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Company(models.Model):
    name = models.CharField(max_length=256, default='')
    logo = models.ImageField(upload_to='logo/', default='/logo/default.png', blank=True)
    summary = models.TextField(default='')
    href = URLOrRelativeURLField(default='/companies/id')
    advocate = models.ManyToManyField(Advocate, blank=True, related_name="advocates")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name