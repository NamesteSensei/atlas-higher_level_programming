#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute the query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display the results
    rows = cur.fetchall()

    # Handle case: No records
    if len(rows) == 0:
        print("No records found.")
    else:
        for row in rows:
            print(row)

    # Close cursor and connection
    cur.close()
    db.close()
