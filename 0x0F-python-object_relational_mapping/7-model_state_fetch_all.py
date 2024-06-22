#!/usr/bin/python3
"""
The script lists all State objects from a database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states():
    """
    Connects to MySQL server, retrieves and lists all State Objects
    from the database sorted by state.id
    """
    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine that stores data in the local MySQL server
    engine = create_engine(
            f'mysql+mysqldb://{mysql_username}:{mysql_password}'
            f'@localhost:3306/{database_name}'
            )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query database
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    list_states()
