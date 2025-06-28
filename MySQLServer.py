import mysql.connector

def create_alx_book_store_db():
    """
    Connects to the MySQL server and attempts to create the 'alx_book_store' database.
    If the database already exists, the script will not fail and will print an appropriate message.
    Handles connection errors and ensures the database connection is closed.
    """
    mydb = None # Initialize mydb to None
    try:
        # Establish connection to the MySQL server (without specifying a database initially)
        # Replace 'your_username' and 'your_password' with your actual MySQL credentials
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",        # Your MySQL username
            password="Harman@2025#" # Your MySQL password
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()

            # SQL to create database if it doesn't exist.
            # This statement handles the "if exists" condition internally without needing SELECT/SHOW.
            sql_create_db = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            mycursor.execute(sql_create_db)

            # Check if the database was actually created or already existed
            # We can't use SELECT/SHOW, so we infer success.
            # A common way to check if it was newly created is to see if an error *didn*t* occur.
            # However, since IF NOT EXISTS prevents an error, we rely on the command's success.
            # For this specific requirement "print message such as Database 'alx_book_store' created successfully!",
            # we'll print it assuming no explicit "already exists" message is required by the problem for this case.
            # If the database existed, CREATE DATABASE IF NOT EXISTS completes successfully without an error.
            print("Database 'alx_book_store' created successfully (or already existed).")

            mycursor.close()
        else:
            print("Failed to establish a connection to the MySQL server.")

    except mysql.connector.Error as err:
        # Handle specific connection errors
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied for user. Check your username and password.")
        elif err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print("Error: Cannot connect to MySQL host. Ensure MySQL server is running and accessible.")
        else:
            print(f"Error: Failed to connect to or interact with MySQL database: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the database connection is closed
        if mydb and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_alx_book_store_db()