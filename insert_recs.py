import sqlite3
from users import users_data

def insert_user_records():
    """Insert all user records from users.py into the users table"""
    
    # Connect to the database
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    
    # Clear existing records (optional - remove if you want to keep existing data)
    cursor.execute('DELETE FROM users')
    
    # Insert each user record
    records_inserted = 0
    for user in users_data:
        try:
            cursor.execute('''
                INSERT INTO users (username, password, auth_level)
                VALUES (?, ?, ?)
            ''', (user['username'], user['password'], user['auth_level']))
            records_inserted += 1
        except sqlite3.Error as e:
            print(f"Error inserting user {user['username']}: {e}")
    
    # Commit the changes
    conn.commit()
    
    # Verify the insertion by counting records
    cursor.execute('SELECT COUNT(*) FROM users')
    total_records = cursor.fetchone()[0]
    
    # Close the connection
    conn.close()
    
    print(f"Successfully inserted {records_inserted} user records!")
    print(f"Total records in users table: {total_records}")

if __name__ == "__main__":
    insert_user_records()
