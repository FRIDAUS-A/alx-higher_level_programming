#!/usr/bin/python3
"""Filters States"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1],
                         sys.argv[2], sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    res = cur.fetchall()
    for value in res:
        if value[1][0] == 'N':
            print(value)
    cur.close()
    db.close()
