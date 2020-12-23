import string
from random import randint

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


fake = Faker()


def password_generator():
    letters = string.ascii_letters
    password = ''
    for i in range(8):
        password += letters[randint(0, len(letters) - 1)]
    return password


class Command(BaseCommand):
    help = 'Adding random users with username, email and password.'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('users_num', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        users_num = options['users_num']
        for i in range(users_num):
            username = fake.first_name() + "_" + fake.last_name()
            email = (username + "@example.com").lower()
            User.objects.create_user(username=username, email=email, password=password_generator())
            self.stdout.write(self.style.SUCCESS(f'Successfully added {username} user'))
