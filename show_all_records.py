import sqlite3

def show_all_records():
    """Display all records from the users table in the people.db database"""
    
    try:
        # Connect to the database
        conn = sqlite3.connect('people.db')
        cursor = conn.cursor()
        
        # Execute query to get all records
        cursor.execute('SELECT * FROM users ORDER BY user_id')
        records = cursor.fetchall()
        
        # Display the results
        if records:
            print("All records in the users table:")
            print("-" * 70)
            print(f"{'ID':<4} {'Username':<25} {'Password':<12} {'Auth Level':<10}")
            print("-" * 70)
            
            for record in records:
                user_id, username, password, auth_level = record
                print(f"{user_id:<4} {username:<25} {password:<12} {auth_level:<10}")
            
            print("-" * 70)
            print(f"Total records: {len(records)}")
        else:
            print("No records found in the users table.")
        
        # Close the connection
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    show_all_records()
