#!/usr/bin/python3

"""

A script that adds the State object “Louisiana”

to the database hbtn_0e_6_usa

"""



import sys

from model_state import Base, State



from sqlalchemy import (create_engine)

from sqlalchemy.orm import sessionmaker



if __name__ == "__main__":

    engine = create_engine(

        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],

                                                    sys.argv[2],

                                                    sys.argv[3])

        )



    Base.metadata.create_all(engine)



    Session = sessionmaker(bind=engine)

    session = Session()



    new_obj = State(name='Louisiana')



    session.add(new_obj)

    session.commit()

    

    print(new_obj.id)

    session.close()
