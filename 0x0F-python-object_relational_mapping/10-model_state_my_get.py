#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_state_by_name():
    """
    Connects to a MySQL server, retrieves and prints the State object
    with the name passed as an argument from the database.
    """
    # Get the MySQL credetials from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Creation of engine storing data in local MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost:3306/{database_name}'
    )

    # Creation of configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query database and retrieve results
    state = session.query(State).filter(State.name == state_name).first()

    # Print results
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close session
    session.close()


if __name__ == "__main__":
    print_state_by_name()
