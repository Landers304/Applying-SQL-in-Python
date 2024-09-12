# Task 1: 


import mysql.connector
from mysql.connector import Error

def add_member(member_id, name, age):
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

            # Query to add a new member
            insert_query = """
                INSERT INTO Members (member_id, name, age)
                VALUES (%s, %s, %s)
            """
            
            # Execute the query
            cursor.execute(insert_query, (member_id, name, age))
            
            # Commit to save the new member
            connection.commit()

            print(f"Member '{name}' added successfully with ID {member_id}.")
    
    except Error as e:
        # Handle duplicates member ID or SQL constraint violation
        if e.errno == 1062:  # Duplicate entry error
            print(f"Error: A member with ID {member_id} already exists.")
        else:
            print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Example 
add_member(1, 'Zachary Landers', 25)




# Task 2:


import mysql.connector
from mysql.connector import Error

def add_workout_session(member_id, date, duration_minutes, calories_burned):
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

            # Query to add a new workout session
            insert_query = """
                INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
                VALUES (%s, %s, %s, %s)
            """
            
            # Execute the SQL query
            cursor.execute(insert_query, (member_id, date, duration_minutes, calories_burned))
            
            # Commit to save the new workout session
            connection.commit()

            print("Workout session added successfully.")

    except Error as e:
        # Handle invalid member ID or SQL constraint violations
        if e.errno == 1452:  # Foreign key fails for invalid i.d.
            print("Error: Invalid member ID. Please provide a valid member.")
        else:
            print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Example
add_workout_session(1, '2024-09-12', 60, 500)



# Task 3:


import mysql.connector
from mysql.connector import Error

def update_member_age(member_id, new_age):
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

            # Query to check if the member exists
            check_member_query = "SELECT COUNT(*) FROM Members WHERE member_id = %s"
            cursor.execute(check_member_query, (member_id,))
            member_exists = cursor.fetchone()[0]

            if member_exists == 0:
                # If the member doesn't exist, return an error message
                print(f"Error: Member with ID {member_id} does not exist.")
                return
            
            # Query to update the member's age
            update_query = "UPDATE Members SET age = %s WHERE member_id = %s"
            cursor.execute(update_query, (new_age, member_id))
            
            # Commit to save the changes
            connection.commit()

            print(f"Member ID {member_id}'s age has been updated to {new_age}.")
    
    except Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Example
update_member_age(1, 30)



# Task 4:


import mysql.connector
from mysql.connector import Error

def delete_workout_session(session_id):
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

            # Query to check if the workout session exists
            check_session_query = "SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(check_session_query, (session_id,))
            session_exists = cursor.fetchone()[0]

            if session_exists == 0:
                # If session doesn't exist, return error message
                print(f"Error: Workout session with ID {session_id} does not exist.")
                return
            
            # Query to delete the workout session
            delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(delete_query, (session_id,))
            
            # Commit to confirm the deletion
            connection.commit()

            print(f"Workout session with ID {session_id} has been deleted.")
    
    except Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Example
delete_workout_session(10)
