from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to="media/%Y-%m-%d", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return "/api/article/%i/" % self.id

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{7,13}$', message="Phone number must be entered in the format: '+375999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=False) # validators should be a list
    message = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        verbose_name_plural = "Feedback"
 
    def __str__(self):
        return self.name + "-" +  self.email
