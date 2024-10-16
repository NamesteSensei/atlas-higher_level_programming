#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306,
        auth_plugin='mysql_native_password'
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the SQL query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and connection to the database
    cur.close()
    db.close()
