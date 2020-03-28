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
    sql = """SELECT cities.name
             FROM states, cities
             WHERE states.id = cities.state_id
             AND states.name = %s
             ORDER BY cities.id ASC"""
    cur = db.cursor()
    cur.execute(sql, (name,))

    query_states = cur.fetchall()

    print(", ".join([row[0] for row in query_states]))

    cur.close()
    db.close()
