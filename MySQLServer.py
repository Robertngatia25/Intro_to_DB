import mysql.connector

def create_alx_book_store_db():
    """
    Connects to the MySQL server and attempts to establish 'alx_book_store' database.
    If the database already exists, this script will complete without error.
    Manages connection errors and ensures database connection closure.
    """
    db_connection = None # Initialize database connection to None
    try:
        # Establish connection to the MySQL server (without a specific database initially)
        # Replace 'your_username' and 'your_password' with your actual MySQL credentials
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",        # Your MySQL username
            password="Harman@2025#" # Your MySQL password
        )

        if db_connection.is_connected():
            db_cursor = db_connection.cursor()

            # SQL command to create database if it is not present.
            # This handles the existence condition internally in MySQL.
            sql_create_database_cmd = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            db_cursor.execute(sql_create_database_cmd)

            # This message indicates successful execution of the CREATE DATABASE command.
            # Since 'IF NOT EXISTS' prevents failure if it exists, this message covers both cases.
            print("Database 'alx_book_store' created successfully!")

            db_cursor.close()
        else:
            print("Failed to establish a connection to the MySQL server.")

    except mysql.connector.Error as err:
        # Handle various connection-related issues
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Verify your username and password.")
        elif err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print("Error: Unable to connect to MySQL host. Confirm server is operational and accessible.")
        else:
            print(f"Error: A database operation issue occurred: {err}")
    except Exception as e:
        print(f"An unexpected problem arose: {e}")
    finally:
        # Guarantee that the database connection is terminated
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("MySQL connection terminated.")

if __name__ == "__main__":
    create_alx_book_store_db()