#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute the query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
