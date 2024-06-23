#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    """
    Connects to a MySQL server, deletes all State objects with name containing
    the letter 'a', and commits the changes to the database
    """
    # Get the MYSQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create  engine that stores data in local MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost:3306/{database_name}'
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query database to retrieve all State objects with a name containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state object
    for state in states_with_a:
        session.delete(state)

    # Commit changes to DB
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
