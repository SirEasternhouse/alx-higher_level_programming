#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana():
    """
    Connects to a MySQL server, adds the State object "Louisiana" to the
    database, and prints the new state's id.
    """
    # Get the MySQL credentials from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creation of engine storing data on local MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost:3306/{database_name}'
    )

    # Creation  of configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Creation of a new State Object
    new_state = State(name="Louisiana")

    # Addition of ne State object to sessin & commit
    session.add(new_state)
    session.commit()

    # Print id of new State object
    print(new_state.id)

    # Close session
    session.close()


if __name__ == "__main__":
    add_louisiana()
