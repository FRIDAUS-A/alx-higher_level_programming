#!/usr/bin/python3
"""A python script to get all the colums in a table"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cur.fetchall()
    for value in result:
        print(value)
    cur.close()
    db.close()
