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

    for state, city in session.query(State, City).\
            join(City).order_by(State.id):
        state_list.append([state.id, state.name])
        city_list.append([city.id, city.name, city.state_id])
    new_list = []
    count = 0
    while (count < len(state_list)):
        value = state_list[count]
        for mem in state_list:
            if value == mem:
                count += 1
        new_list.append(value)
    state_list.clear()
    for state in new_list:
        print(f"{state[0]}: {state[1]}")
        for city in city_list:
            if state[0] == city[2]:
                print(f"    {city[0]}: {city[1]}")
