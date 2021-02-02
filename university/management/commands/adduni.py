import string
import time
from random import randint, random

from django.core.management.base import BaseCommand

from faker import Faker

from university.models import Student, University


fake = Faker()


def random_date(start, end, t_format, prop):
    stime = time.mktime(time.strptime(start, t_format))
    etime = time.mktime(time.strptime(end, t_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(t_format, time.localtime(ptime))


def university_name_generator():
    letters = string.ascii_uppercase
    name = 'Kh'
    for i in range(randint(3, 6)):
        name += letters[randint(0, len(letters) - 1)]
    return name


class Command(BaseCommand):
    help = 'Adding random universities and studets.'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('users_num', type=int, choices=range(1, 501))

    def handle(self, *args, **options):
        users_num = options['users_num']
        for i in range(users_num):

            uni = University(
                name=university_name_generator(),
                date_of_found=random_date("1890-01-01", "2000-01-01", '%Y-%m-%d', random())
            )

            uni.save()

            for i in range(10):
                first_name = fake.first_name()
                last_name = fake.last_name()
                date_of_birth = random_date("1998-01-01", "2002-01-01", '%Y-%m-%d', random())
                Student.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    date_of_birth=date_of_birth,
                    university=uni
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully added {first_name} student {uni.name}'))
