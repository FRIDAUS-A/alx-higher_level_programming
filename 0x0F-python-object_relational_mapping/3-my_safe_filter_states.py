#!/usr/bin/python3
"""SQL Injection..."""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1],
                         sys.argv[2], sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s\
                ORDER BY id ASC", (sys.argv[4], ))
    res = cur.fetchall()
    for value in res:
        print(value)
    cur.close()
    db.close()
