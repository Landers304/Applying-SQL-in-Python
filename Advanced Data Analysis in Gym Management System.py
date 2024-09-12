# Task 1:

import mysql.connector
from mysql.connector import Error

def get_members_in_age_range(start_age, end_age):
    try:
        # Establish connection to the database
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='MYSQL',
            user='root',
            password='Password'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Query to retrieve members age between start_age and end_age
            query = """
                SELECT member_id, name, age 
                FROM Members 
                WHERE age BETWEEN %s AND %s
            """
            
            # Execute the query
            cursor.execute(query, (start_age, end_age))
            
            # Fetch all results
            results = cursor.fetchall()

            if results:
                print("Members between ages", start_age, "and", end_age, ":")
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
            else:
                print(f"No members found between ages {start_age} and {end_age}.")
    
    except Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Example 
get_members_in_age_range(25, 30)
