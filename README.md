# Python-Command-Line-Language-FlashCards

This is a flash card CLI application made with Python and PostgreSQL. The flash cards are based on the topic of learning or studying a language. In this case you are given different russian verbs and need to be able to translate them to English. 

When the application is ran you will be giving a main menu where you can decide what you would like to do. The application gives you the option to study the flashcards or to create a new card. As shown below.

![Imgur](https://i.imgur.com/30ddKOw.png)


#  Main Installation
Make sure to have Python3, SQL, Peewee and PostgresSql installed.

- Clone this repository
   
    >       git clone 

- Install dependencies
   
    >       pipenv install peewee psycopg2-binary autopep8  
    
- Run your virtual environment
    
    >      pipenv shell

- To access the flashcards, run the command in your shell.
    
    >       python main.py or python3 main.py

#  Database Connection

- PostgresSql database connection
  
   >        psql -d postgres 

- Navigation in Postgres commands
   ``` 
    - Create
         >> CREATE DATABASE FLASHCARDS2;
    
    - Connect
         >> \c flashcards2;

    - View data list table
         >>  \d 

    - To view table list of flashcards
         >> select * from flashcard;
         
   ```

## Feature upcomings
- Update and delete functionality
    