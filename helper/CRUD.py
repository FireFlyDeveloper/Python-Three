import sqlite3
from sqlite3 import Error
from models.SQLquery import SQLquery

class CRUD:
    DB_PATH = "three.db"  # SQLite database file

    def connect(self):
        """Connect to the SQLite database and return the connection."""
        try:
            connection = sqlite3.connect(self.DB_PATH)  # Connect to the SQLite database
            print("Connected to the SQLite database!")
            return connection
        except Error as e:
            print(f"Connection failed! {e}")
        return None

    def create_table(self):
        """Create the 'users' table if it doesn't already exist."""
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                number TEXT NOT NULL,
                email TEXT NOT NULL,
                price REAL NOT NULL,
                date TEXT NOT NULL,
                done BOOLEAN DEFAULT FALSE,
                queue_type TEXT NOT NULL DEFAULT 'regular'  -- Adding a 'queue_type' column for differentiation
            )
        """
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                print("Table 'users' created successfully (if it didn't already exist).")
            except Error as e:
                print(f"Error during CREATE TABLE operation: {e}")
            finally:
                cursor.close()
                connection.close()

    def create(self, sql_query):
        """Insert a new user into the database."""
        query = """
            INSERT INTO users (name, number, email, price, date, done, queue_type) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, (sql_query.name, sql_query.number, 
                                       sql_query.email, sql_query.price, 
                                       sql_query.date, sql_query.done, 
                                       sql_query.queue_type))  # Include queue_type
                connection.commit()
                print("A new user was inserted successfully!")
                return True
            except Error as e:
                print(f"Error during CREATE operation: {e}")
            finally:
                cursor.close()
                connection.close()
        return False

    def read(self):
        """Read all users from the database."""
        query = "SELECT * FROM users"
        users = []
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                result_set = cursor.fetchall()
                for row in result_set:
                    # Assuming SQLquery accepts the updated structure (including queue_type)
                    user = SQLquery(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])  # Updated to include queue_type
                    users.append(user)
            except Error as e:
                print(f"Error during READ operation: {e}")
            finally:
                cursor.close()
                connection.close()
        return users

    def get_last_inserted_id(self):
        """Get the ID of the last inserted user."""
        query = "SELECT MAX(id) AS max_id FROM users"
        last_id = 0
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                result_set = cursor.fetchone()
                if result_set:
                    last_id = result_set[0]
            except Error as e:
                print(f"Error during SELECT operation: {e}")
            finally:
                cursor.close()
                connection.close()
        return last_id

    def update(self, sql_query):
        """Update an existing user in the database."""
        query = """
            UPDATE users 
            SET name = ?, number = ?, email = ?, price = ?, date = ?, done = ?, queue_type = ? 
            WHERE id = ?
        """
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, (sql_query.name, sql_query.number, sql_query.email, 
                                       sql_query.price, sql_query.date, sql_query.done, 
                                       sql_query.queue_type, sql_query.id))  # Updated to include queue_type
                connection.commit()
                print(f"User with ID {sql_query.id} was updated successfully!")
                return True
            except Error as e:
                print(f"Error during UPDATE operation: {e}")
            finally:
                cursor.close()
                connection.close()
        return False

    def delete_last_inserted(self):
        """Delete the last inserted user from the database."""
        select_query = "SELECT id FROM users ORDER BY id DESC LIMIT 1"
        last_inserted_id = -1
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(select_query)
                result_set = cursor.fetchone()
                if result_set:
                    last_inserted_id = result_set[0]
            except Error as e:
                print(f"Error during SELECT operation: {e}")
                return False
            finally:
                cursor.close()

        if last_inserted_id != -1:
            delete_query = "DELETE FROM users WHERE id = ?"
            connection = self.connect()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute(delete_query, (last_inserted_id,))
                    connection.commit()
                    print("Last inserted record was deleted successfully.")
                    return True
                except Error as e:
                    print(f"Error during DELETE operation: {e}")
                finally:
                    cursor.close()
                    connection.close()
        return False

    def clear(self):
        """Clear all records from the 'users' table."""
        query = "DELETE FROM users"
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                print("All records have been cleared.")
                return True
            except Error as e:
                print(f"Error during CLEAR operation: {e}")
            finally:
                cursor.close()
                connection.close()
        return False
    
    def setup(self):
        """Ensure the database and table are created."""
        self.connect()  # This will create the database file if it doesn't exist
        self.create_table()  # Create the necessary table if it doesn't exist