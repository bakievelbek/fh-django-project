import datetime

from django.db import models

CATEGORIES = (
    ('student', 'Student'),
    ('professor', 'Professor')
)


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField(default=datetime.date.today)
    role = models.CharField(choices=CATEGORIES, max_length=20)

    email = models.CharField(max_length=128, unique=True)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    post_number = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)

    class Meta:
        db_table = 'fh_user'
        app_label = 'app'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
