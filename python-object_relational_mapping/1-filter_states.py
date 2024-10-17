#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_password, db=db_name)

    # Create a cursor to execute queries
    cur = db.cursor()

    # SQL query to select states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all results
    rows = cur.fetchall()

    # Print each row in the required format
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
