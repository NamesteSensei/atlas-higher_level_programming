#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
