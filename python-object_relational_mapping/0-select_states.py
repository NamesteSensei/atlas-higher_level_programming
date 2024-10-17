#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],  # MySQL username
        passwd=sys.argv[2],  # MySQL password
        db=sys.argv[3],  # Database name
        port=3306
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query to retrieve all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
