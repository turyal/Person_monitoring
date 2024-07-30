import sqlite3
from datetime import datetime, timedelta
import csv

def fetch_and_write_activities_to_csv():
    """Fetch activities from the database, expand the duration to per-second rows, and write to a CSV file."""
    connection = sqlite3.connect('ruyi.db')
    cursor = connection.cursor()

    # Fetch all rows from the activities table
    cursor.execute("SELECT * FROM activities ORDER BY start_time")
    rows = cursor.fetchall()

    csv_rows = []

    new_id = 1  # Initialize a new ID for the expanded rows

    for row in rows:
        id, start_time, end_time, activity, place = row
        start_time = datetime.fromisoformat(start_time)
        end_time = datetime.fromisoformat(end_time)

        current_time = start_time
        while current_time <= end_time:
            formatted_timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
            formatted_date = current_time.strftime('%Y-%m-%d')
            formatted_time = current_time.strftime('%H:%M:%S')
            csv_rows.append([new_id, formatted_timestamp,formatted_date,formatted_time, activity, place])
            new_id += 1
            current_time += timedelta(seconds=1)

    # Write to CSV file
    with open('activities.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'timestamp','Date','Time', 'Activity', 'Place'])  # Write the header
        writer.writerows(csv_rows)  # Write the data rows

    connection.close()

if __name__ == '__main__':
    fetch_and_write_activities_to_csv()
