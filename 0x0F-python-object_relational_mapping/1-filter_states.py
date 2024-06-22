#!/usr/bin/python3
"""
Listing all states starting with "N" from database
"""


import MySQLdb
import sys


def list_states_starting_with_n():
    """
    Connects to MySQL server,retrieves and lists all states
    starting with 'N' from database.
    """

    # Get credentials from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Creating cusor to execute queries
    cursor = db.cursor()

    # Executing quey for states that sart with 'N' sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows in a lists of lists
    rows = cursor.fetchall()

    # Print rows
    for row in rows:
        print(row)

    # CLose cursor & DB connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_starting_with_n()
