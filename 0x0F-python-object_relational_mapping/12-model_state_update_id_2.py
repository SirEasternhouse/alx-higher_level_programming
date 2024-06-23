#!/usr/bin/python3
"""
This script changes the name of a State object from the database.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name():
    """
    Connects to a MySQL server, changes the name of the State object with id=2
    to "New Mexico", and commits the change to the database.
    """
    # Get the MySQL credentials from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creation of engine to store data in local MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost:3306/{database_name}'
    )

    # Creattion of configured "Session" class
    Session = sessionmaker(bind=engine)

    # Creation of Session
    session = Session()

    # Query database to retrieve object with id=2
    state = session.query(State).filter_by(id=2).first()

    # Changinf the name of the stae to "New Mexico"
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    change_state_name()
