from mongoengine import *
from tvsr.settings import DBNAME

connect(DBNAME)

class Movie(Document):
    title = StringField(max_length=120, required=True)
    director = StringField(max_length=120, required=True)
    img_name = StringField(max_length=120, required=True)    
    subject_id = StringField(max_length=120, required=True)
    
# Create your models here.
