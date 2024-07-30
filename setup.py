import sqlite3

def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
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

    # Create Activities Table with place column
    try:
        cursor.execute('''
        CREATE TABLE activities (
            id INTEGER PRIMARY KEY,
            start_time TIMESTAMP,
            end_time TIMESTAMP,
            activity TEXT,
            place TEXT
        )
        ''')
    except sqlite3.Error as e:
        if "already exists" in str(e):
            print('table activities already exists, altering table to add place column if it does not exist')
            try:
                cursor.execute("ALTER TABLE activities ADD COLUMN place TEXT")
            except sqlite3.Error as e:
                if "duplicate column name" in str(e):
                    print('column place already exists')
                else:
                    print(e)

    # Create Trigger Table
    try:
        cursor.execute('''
        CREATE TABLE triggers (
            id INTEGER PRIMARY KEY,
            time TIMESTAMP,
            trigger_type TEXT
        )
        ''')
    except sqlite3.Error as e:
        if "already exists" in str(e):
            print('table triggers already exists')

    # Create Sound Classifications Table
    try:
        cursor.execute('''
        CREATE TABLE sound_classifications (
            id INTEGER PRIMARY KEY,
            start_time TIMESTAMP,
            end_time TIMESTAMP,
            sound TEXT
        )
        ''')
    except sqlite3.Error as e:
        if "already exists" in str(e):
            print('table sound_classifications already exists')

    # Create Gait Table
    try:
        cursor.execute('''
        CREATE TABLE gait (
            timestamp TIMESTAMP PRIMARY KEY,
            id INTEGER,
            file_path TEXT
        )
        ''')
    except sqlite3.Error as e:
        if "already exists" in str(e):
            print('table gait already exists')

    # Create Patient Table
    try:
        cursor.execute('''
        CREATE TABLE patient (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            fall_fear BOOLEAN
        )
        ''')
    except sqlite3.Error as e:
        if "already exists" in str(e):
            print('table patient already exists')

    # Commit the changes
    connection.commit()
    connection.close()
