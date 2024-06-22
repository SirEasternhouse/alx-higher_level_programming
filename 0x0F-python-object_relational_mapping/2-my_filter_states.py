#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table where name matches the argument.
"""

import MySQLdb
import sys


def display_states_with_name():
    """
    Connects to a MySQL server, retrieves and lists all states
    where the name matches the argument.
    """
    # Get the MySQL credentials from the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the query  retrieving states name matching  arg sorted by id
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and db connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    display_states_with_name()
