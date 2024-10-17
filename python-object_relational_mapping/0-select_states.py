#!/usr/bin/python3
import MySQLdb
import sys
import os

if __name__ == "__main__":
    # Capture arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=os.getenv('MYSQL_PWD'),  # Use environment variable for password
        db=sys.argv[2]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
