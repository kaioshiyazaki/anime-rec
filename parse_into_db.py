import csv
import sqlite3

def parse_csv_to_sqlite(csv_file, db_file):
    # Connecting to the SQLite database
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS anime_data (
                anime_id INTEGER PRIMARY KEY, 
                name TEXT,
                genre TEXT,
                type TEXT,
                episodes INTEGER,
                rating REAL,
                members INTEGER
            )
        ''')

        # Open the CSV file with UTF-8 encoding (avoiding encoding errors)
        with open(csv_file, 'r', encoding='utf-8') as file:
            # Creating a CSV reader object
            csv_reader = csv.reader(file)

            # Skip the header row
            next(csv_reader)

            # Prepare a list to store all rows for batch insertion
            all_rows = []

            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Ensure the row has exactly the number of expected fields
                if len(row) == 7:
                    all_rows.append(row)
                else:
                    print(f"Skipping malformed row: {row}")

            # Insert all rows into the database in a single operation
            try:
                cursor.executemany("INSERT INTO anime_data VALUES (?, ?, ?, ?, ?, ?, ?)", all_rows)
            except sqlite3.DatabaseError as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Exception in inserting rows: {e}")

csv_file = 'anime.csv'
db_file = 'anime.db'
parse_csv_to_sqlite(csv_file, db_file)
