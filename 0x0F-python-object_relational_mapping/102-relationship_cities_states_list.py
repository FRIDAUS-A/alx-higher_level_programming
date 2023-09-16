#!/usr/bin/python3
"""
a script that lists all City objects
from the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
