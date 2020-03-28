#!/usr/bin/python3
"""script that takes in the name
of a state as an argument and lists
all cities of that state, using
the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    name = sys.argv[4]
    sql = """SELECT id, name
             FROM cities
             WHERE state_id =
                   (SELECT id
                    FROM states
                    WHERE `name` = %s) ORDER BY id ASC;"""
    cur = db.cursor()
    cur.execute(sql, (name,))

    query_rows = cur.fetchall()

    for row in range(len(query_rows)):
        if row != (len(query_rows) - 1):
            print(query_rows[row][1], end=", ")
        else:
            print(query_rows[row][1])
    cur.close()
    db.close()
