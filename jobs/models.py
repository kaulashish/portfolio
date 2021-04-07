from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50, default="Project " + str(id))
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=255)
    started = models.DateField(null=True, blank=True)
    ended = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.summary


class Detail(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    location = models.TextField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return str("Ashish's details")


class Education(models.Model):
    graduation = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    field = models.CharField(max_length=20)
    college = models.CharField(max_length=70)
    marks = models.FloatField(max_length=3)

    def __str__(self):
        return self.graduation


class Accomplishments(models.Model):
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text


class Skills(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill
