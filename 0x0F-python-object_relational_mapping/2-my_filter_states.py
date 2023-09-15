#!/usr/bin/python3
"""Filter states by user input"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1],
                         sys.argv[2], sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=BINARY '{}'\
                ORDER BY id ASC".format(sys.argv[4]))
    res = cur.fetchall()
    for value in res:
        print(value)
    cur.close()
    db.close()
