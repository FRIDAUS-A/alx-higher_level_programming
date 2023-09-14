#!/usr/bin/python3
import sys
import MySQLdb
db = MySQLdb.connect(host='localhost', user=sys.argv[1], 
    password=sys.argv[2], database=sys.argv[3], port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
result = cur.fetchall()
for value in result:
    print(value)
