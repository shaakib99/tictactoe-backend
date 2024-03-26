from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session
from sqlalchemy import create_engine


from load_env import env


class Base(DeclarativeBase):
    pass


engine = create_engine(
    env.get("DATABASE_URL", "mysql://root:root@localhost:3306/tic_tac_toe_dev")
)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory=session_factory)


def get_db():
    # create all tables
    Base.metadata.create_all(bind=engine)

    # create connection
    db = Session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()
