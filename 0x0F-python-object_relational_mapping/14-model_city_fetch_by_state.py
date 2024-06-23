#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state():
    """
    Connects to a MySQL server, fetches all City objects, and prints them
    in the format: <state name>: (<city id>) <city name>
    """
    # Get the MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to store data in local MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost:3306/{database_name}'
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query database to retrieve all City objects and join with State objects
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
