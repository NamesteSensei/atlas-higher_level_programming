#!/usr/bin/python3
"""
Script that lists all states where 'name' matches the argument from the
database 'hbtn_0e_0_usa'. Uses MySQLdb to connect to MySQL server.
Arguments:
    mysql username (sys.argv[1])
    mysql password (sys.argv[2])
    database name (sys.argv[3])
    state name (sys.argv[4])
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

    # SQL query to find states by name (case-sensitive)
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        .format(state_name)
    )

    # Execute the query and fetch results
    cur.execute(query)
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
