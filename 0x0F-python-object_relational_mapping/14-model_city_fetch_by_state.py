#!/usr/bin/python3
"""script that lists all states objects"""

import sys
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst, ance in session.query(City, State).filter(State.id==City.state_id).order_by(City.state_id):
        print("{}: ({}) {}".format(ance.name, inst.id, inst.name))
    session.close()  
