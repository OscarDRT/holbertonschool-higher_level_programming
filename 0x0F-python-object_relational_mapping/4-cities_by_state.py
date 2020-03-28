#!/usr/bin/python3
"""
    cript that lists all cities
    from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    sql = """SELECT cities.id, cities.name, states.name
             FROM cities JOIN states
             ON cities.state_id = states.id ORDER BY cities.id ASC"""
    cur = db.cursor()
    cur.execute(sql)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
