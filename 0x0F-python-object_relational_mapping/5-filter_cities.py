#!/usr/bin/python3
"""All ciies by state"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1],
                         sys.argv[2], sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities AS c\
                JOIN states AS s ON c.state_id = s.id\
                WHERE s.name = %s ORDER BY c.id ASC",
                (sys.argv[4], ))
    res = cur.fetchall()
    count = 0
    for value in res:
        for mem in value:
            print(f"{mem}", end="")
            if (count != len(res) - 1):
                print(", ", end="")
            count += 1
    print()
