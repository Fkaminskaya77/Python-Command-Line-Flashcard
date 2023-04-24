from peewee import *
# import IPython

# Create DB connection
db = PostgresqlDatabase(
'flashcards2',
user='', 
password='',
host='localhost', 
port=5432
)

db.connect()

#models
class BaseModel(Model):
    class Meta:
        database = db

class FlashCard(BaseModel):
    russian_word = CharField()
    english_word= CharField()

# IPython.embed()