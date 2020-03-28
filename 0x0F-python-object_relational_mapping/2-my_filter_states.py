#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    name = sys.argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                   WHERE states.name LIKE BINARY'{}%'
                   ORDER BY states.id ASC""".format(name))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
