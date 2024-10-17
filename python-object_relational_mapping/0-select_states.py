#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the SQL query to retrieve all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results of the query
    states = cur.fetchall()

    # Loop through the states and print them one by one
    for state in states:
        print(state)

    # Close the cursor and database connection
    cur.close()
    db.close()
