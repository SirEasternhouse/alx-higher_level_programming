#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


def list_cities_of_state():
    """
    Connects to MySQL server lists all cities given a state
    """
    # Getting credentials from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_password,
        db=database_name
    )

    # Creating a cursor to execute queries
    cursor = db.cursor()

    # Execute the query
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # fetch all rows in a list
    rows = cursor.fetchall()

    # Printing the rows as a comma- separated string
    print(", ".join(row[0] for row in rows))

    # closing cursor and db connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_of_state()
