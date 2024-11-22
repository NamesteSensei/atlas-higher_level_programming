#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
Takes in 4 arguments: mysql username, mysql password, database name, and state name (SQL injection free).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute queries
    cur = db.cursor()

    # SQL query to find cities in a given state (SQL injection free)
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """

    # Execute the query with the state name as a parameter
    cur.execute(query, (state_name,))

    # Fetch all the results
    cities = cur.fetchall()

    # Print the city names, separated by commas
    print(", ".join(city[0] for city in cities))

    # Close the cursor and connection
    cur.close()
    db.close()
