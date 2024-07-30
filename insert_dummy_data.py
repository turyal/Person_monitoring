import sqlite3
import random
from datetime import datetime, timedelta

def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(f"SQLite version: {sqlite3.sqlite_version}")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_sqlite_database('ruyi.db') 
    connection = sqlite3.connect('ruyi.db')
    
    # Create a cursor object
    cursor = connection.cursor()

    # Define the list of activity types
    activities_list = [ 'Laying','Sitting', 'Standing', 'Walking','Walking','Standing',]
    
    places_list = ['Room', 'Room', 'Room','Room','Lounge', 'Lounge',]

    # Define the list of sound types
    sounds_list = ['scream', 'snore', 'silence']

    # Function to insert a new activity record
    def insert_activity(cursor, start_time, end_time, activity, place):
        cursor.execute('''
        INSERT INTO activities (start_time, end_time, activity, place)
        VALUES (?, ?, ?, ?)
        ''', (start_time, end_time, activity, place))

    # Function to insert a new sound classification record
    def insert_sound_classification(cursor, start_time, end_time, sound):
        cursor.execute('''
        INSERT INTO sound_classifications (start_time, end_time, sound)
        VALUES (?, ?, ?)
        ''', (start_time, end_time, sound))

    activitity_index = -1
    # Insert 1200 rows into the activities table FOR 1 HOUR
    for i in range(1200):
        start_time = datetime.now() + timedelta(seconds=i * 3)
        end_time = start_time + timedelta(seconds=3)  # Each activity lasts for 3 seconds
        if i % 200 == 0:
            activitity_index += 1
        activity = activities_list[activitity_index] 
        place = places_list[activitity_index] 
        insert_activity(cursor, start_time, end_time, activity, place)

    # Insert 10800 rows into the sound_classifications table
    for i in range(10800):
        start_time = datetime.now() + timedelta(seconds=i)
        end_time = start_time + timedelta(seconds=1)  # Each sound classification lasts for 1 second
        sound = random.choice(sounds_list)  # Randomly choose a sound
        insert_sound_classification(cursor, start_time, end_time, sound)

    # Insert 1 row into gait table
    cursor.execute('''
        INSERT INTO gait (timestamp, id, file_path)
        VALUES (?, ?, ?)
        ''', (datetime.now(), 1, './data.csv'))

    # Commit the changes
    connection.commit()
    connection.close()

    print("Inserted 1200 rows into the 'activities' table.")
    print("Inserted 10800 rows into the 'sound_classifications' table.")
