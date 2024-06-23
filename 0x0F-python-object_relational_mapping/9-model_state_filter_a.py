#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from a database.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a():
    """
    Connects to a MySQL server, retrieves and lists all State objects
    that contain the letter 'a' from the database sorted by state.id.
    """
    # Get the My SQL credentials from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creating engine storing data in local MySQL server
    engine = create_engine(
            f'mysql+mysqldb://{mysql_username}:{mysql_password}'
            f'@localhost:3306/{database_name}'
    )

    # Creatio of configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query database retrieving results
    states = session.query(State).filter(
            State.name.ilike('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    list_states_with_a()
