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

# Creating Tables for database
db.create_tables([FlashCard])

# Seed the database with data
card1 = FlashCard(russian_word = 'да (da)', english_word = 'yes')
card1.save()

# IPython.embed()