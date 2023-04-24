from peewee import *

# Create DB connection
db = PostgresqlDatabase(
'flashcards2',
user='', 
password='',
host='localhost', 
port=5432
)

db.connect()