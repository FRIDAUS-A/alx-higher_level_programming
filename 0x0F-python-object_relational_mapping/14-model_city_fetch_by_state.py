#!/usr/bin/python3
"""
a Python file similar to model_state.py named
model_City.py that contains the class definition of a City.
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State.name.label('statename'), City.id,
                                  City.name.label('cityname')).\
            filter(State.id == City.state_id).\
            order_by(City.id).all():
        print(f"{instance.statename}: ({instance.id}) {instance.cityname}")
