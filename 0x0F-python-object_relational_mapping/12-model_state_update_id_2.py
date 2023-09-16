#!/usr/bin/python3
"""
a script that changes the name of a State
object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.id == 2):
        instance.name = 'New Mexico'
    session.commit()
