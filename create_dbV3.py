"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os 
import sqlite3   
from datetime import datetime  
from faker import Faker 

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    # Opens a connection to an SQLite database.
    # Returns a Connection object that represent the database connection.
    # A new database file will be created if it doesn't exist.
    con= sqlite3.connect('social_network.db') 
    
    # Get a Cursor object that can be used to run SQL queries on the database.
    cur = con.cursor()   
    
    # Define an SQL query that creates a table named 'people'.
    # Each row in this table will hold information about a specific person.
    
    people_table_query = """
    
       CREATE TABLE IF NOT EXISTS people
       (
          id        INTEGER PRIMARY KEY,
          name      TEXT NOT NULL,
          email     TEXT NOT NULL,
          address   TEXT NOT NULL,
          city      TEXT NOT NULL,
          province  TEXT NOT NULL,
          bio       TEXT,
          age       INTEGER,
          created_at DATETIME NOT NULL,
          updated_at DATETIME NOT NULL    
       );         
    """
    # Execute the SQL query to create the 'people' table.
    # Database operations like this are called transactions.
    cur.execute(people_table_query)    
    
    # Commit (save) pending transactions to the database.
    # Transactions must be committed to be persistent.
    con.commit()
    
    # Close the database connection.
    con.close()   
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    
    con = sqlite3.connect('social_network.db') 
    cur = con.cursor() 
    
    # Define an SQL query that inserts a row of data in the people table.
    # The ?'s are placeholders to be fill in when the query is executed.
    # Specific values can be passed as a tuple into the execute() method.
    
    # Create a faker object for English Canadian locale
    fake = Faker("en_CA")
    add_ppl_query = """
          INSERT INTO people
          (
              name,
              email,
              address,
              city,
              province,
              bio,
              age,
              created_at,
              updated_at
          )
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    
    # Generate fake data for 200 people
    for i in range(200):  
       new_person = (
                      fake.name(),
                      fake.email(),
                      fake.address(),
                      fake.city(),
                      fake.province(),
                    #  'Enjoys making funny sounds when talking.',
                      fake.random_int(min=18, max=99),
                      datetime.now(),
                      datetime.now()
            )
       cur.execute(add_person_query,new_person)
    con.commit()
    con.close()
 
# Define a tuple of data for the new person to insert into people table
# Data values must be in the same order as specified in query
    return 

if __name__ == '__main__':
   main()
