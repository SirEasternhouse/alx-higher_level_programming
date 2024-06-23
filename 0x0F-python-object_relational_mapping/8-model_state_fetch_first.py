#!/usr/bin/python3
"""
Script prints the first State Object from the database.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state():
    """
    Connects to a MyQL server, retrieves & prints the first stae object
    from the database sorted by state.id.
    """
    # GEt MySQL credentials from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creation of engine that stores data in local MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost:3306/{database_name}'
    )

    # Creation of a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query database to retireve results
    first_state = session.query(State).order_by(State.id).first()

    # Print result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()


if __name__ == "__main__":
    print_first_state()
