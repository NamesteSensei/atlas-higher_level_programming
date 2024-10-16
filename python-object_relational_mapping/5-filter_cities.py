#!/usr/bin/python3
"""
A script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor to execute queries
    cur = db.cursor()

    # Use parameterized query to avoid SQL injection
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch and display the results
    rows = cur.fetchall()

    # Print the city names comma-separated
    print(", ".join(row[0] for row in rows))

    # Close cursor and connection
    cur.close()
    db.close()
