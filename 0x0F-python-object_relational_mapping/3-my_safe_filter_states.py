#!/usr/bin/python3
"""Free injection"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    name = sys.argv[4]
    sql = """SELECT * FROM states
                      WHERE states.name LIKE BINARY %s
                      ORDER BY states.id ASC"""
    cur = db.cursor()
    cur.execute(sql, (name,))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
