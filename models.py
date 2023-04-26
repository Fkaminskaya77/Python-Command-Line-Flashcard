from peewee import *



db = PostgresqlDatabase(
'flashcards2',
user='', 
password='',
host='localhost', 
port=5432
)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db

class FlashCard(BaseModel):
    russian_word = CharField()
    english_word= CharField()
    hint = CharField(null=True)

