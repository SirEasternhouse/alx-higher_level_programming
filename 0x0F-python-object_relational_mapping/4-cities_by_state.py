#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


def list_cities():
    """
    Connects to a MySQL server,retrieves and lists all citites from the db.
    """
    # Get the MySQL credetials from the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Creating cursor to execute queries
    cursor = db.cursor()

    # Executing query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all rows in a list of lists
    rows = cursor.fetchall()

    # Printing the rows
    for row in rows:
        print(row)

    # Close DB conection and cursor
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
