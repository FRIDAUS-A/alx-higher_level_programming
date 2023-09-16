#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and
save them as relationship_city.py and relationship_state.py
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3],
                            pool_pre_ping=True))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="California")
    newCity = City(name="San Fancisco")
    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
