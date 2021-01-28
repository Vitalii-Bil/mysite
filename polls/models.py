import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name


class Log(models.Model):
    path = models.CharField(max_length=2048)
    method = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.path}, {self.method}, {self.timestamp}"


class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)
    about = models.CharField(_("about"), max_length=5000)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Quote(models.Model):
    quote = models.CharField(_("quote"), max_length=200)
    tags = models.CharField(_("tags"), max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.quote
