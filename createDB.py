import sqlite3

# Create the database and users table
def create_database():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    
    # Create the users table with the specified schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            auth_level INTEGER NOT NULL
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Database 'people.db' created successfully!")
    print("Table 'users' created with the following schema:")
    print("- user_id: INTEGER PRIMARY KEY AUTOINCREMENT")
    print("- username: TEXT")
    print("- password: TEXT")
    print("- auth_level: INTEGER")

if __name__ == "__main__":
    create_database()
