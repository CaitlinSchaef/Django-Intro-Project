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
import random 

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


# object_list = Author.objects.bulk_create(
#     [
#         Author(name='Mary Shelly'),
#         Author(name='Grand Dam'),
#         Author(name='Aldus Huxley'),
#         Author(name='Burger Boy'),
#         Author(name='Prim Proper'),
#         Author(name='Squeaky Clean'),
#         Author(name='Emily Bronte'),
#         Author(name='Ovid')
#     ]
# )

# authors = Author.objects.all()
# for author in authors:
#     print(author)

# object_list = Book.objects.bulk_create(
#     [
#         Book(title='Where The Sidewalk Ends', published_date=2022),
#         Book(title='Metamorphoses', published_date=0000),
#         Book(title='The Odyssey', published_date=120),
#         Book(title='Letters to Lucilius', published_date=560),
#         Book(title='The Wizard of Oz', published_date=1945),
#         Book(title='RedWall', published_date=2002),
#         Book(title='Wicked', published_date=2008),
#         Book(title='Call of the Wild', published_date=1876),
#         Book(title='Pride and Prejudice', published_date=1771),
#         Book(title='Brave New World', published_date=1872),
#         Book(title='Red Fish, Blue Fish', published_date=1946),
#         Book(title='Handmaids Tail', published_date=2005),
#         Book(title='Llama Llama Red Pajama', published_date=2006),
#         Book(title='The Outsiders', published_date=1956)
#     ]
# )

# books = Book.objects.all()
# for book in books:
#     print(book)

books = Book.objects.all()
for b in books:    
    author_name = random.choice(Author)
    #getting an error at the random.choice, made it just Author, so this should give a random author
    #then we need to apply that
    b.author = author_name
    b.save()