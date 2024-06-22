#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys


def list_states():
    """
    Connects to a MySQL server, retrieves and lists all states from database.
    """
    # Getting Mysql username, password and DB name from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connecting to th MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
            )

    # Creating a cursor to execute queries
    cursor = db.cursor()

    # Execute query to retrieve states sortd by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # Printing rows
    for row in rows:
        print(row)

    # close cusor & db connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
