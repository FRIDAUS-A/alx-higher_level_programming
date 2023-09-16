#!/usr/bin/python3
"""
a script that lists all State objects, and
corresponding City objects, contained in
the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, aliased

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_list = list()
    city_list = []

    for state in session.query(State):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
