#!/usr/bin/python3
"""
A script that displays all values in the states table where name matches the argument,
and is safe from SQL injection.
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

    # Use parameterized query to prevent SQL injection
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

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
