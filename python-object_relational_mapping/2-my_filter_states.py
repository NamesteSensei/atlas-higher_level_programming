#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments: mysql username, mysql password, database name, state name
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    # Use format to create SQL query with user input safely
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

