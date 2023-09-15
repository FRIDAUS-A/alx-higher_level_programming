#!/usr/bin/python3
"""Cties by states"""

import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1],
                         sys.argv[2], sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities AS c\
                 JOIN states AS s ON c.state_id = s.id ORDER BY c.id ASC")
    res = cur.fetchall()
    for value in res:
        print(value)
    cur.close()
    db.close()
