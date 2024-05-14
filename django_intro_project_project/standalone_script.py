import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "django_intro_project_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

from django_intro_project_app.models import *

# object_list = Reader.objects.bulk_create(
#     [
#         Reader(name='Marcus Schaeffer', state='Kentucky'),
#         Reader(name='Caitlin Schaeffer', state='Kentucky'),
#         Reader(name='Lana Schaeffer', state='Indiana'),
#         Reader(name='Joe Schaeffer', state='Indiana'),
#         Reader(name='Joe Shmoe', state='Arizona'),
#         Reader(name='Meg Wilkins', state='Alabama'),
#         Reader(name='Murphy Brown', state='Alaska'),
#         Reader(name='Bob Rough', state='Michigan'),
#         Reader(name='Temperance Brennan', state='West Virginia'),
#         Reader(name='Aristotle Bugger', state='Missouri'),
#         Reader(name='Plato Smith', state='Missouri'),
#         Reader(name='Megan Griffin', state='Arizona'),
#         Reader(name='Kate Blanchette', state='Arizona'),
#         Reader(name='Chris Traeger', state='Michigan'),
#         Reader(name='Bear Trapper', state='Alaska'),
#         Reader(name='Doris Day', state='New York'),
#         Reader(name='Frank Sinatra', state='New York'),
#         Reader(name='Eedy Bachofner', state='Washington'),
#         Reader(name='Trevor Bachofner', state='Washington'),
#         Reader(name='Andrea Holderman', state='Arkansas'),
#     ]
# )
#you accidentally ran this twice which is not great

# readers = Reader.objects.all()
# for reader in readers:
#     print(reader)



