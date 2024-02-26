from sqlalchemy import create_engine
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/cdc_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

db: Session = Session(bind=engine)

def close_conn(db: Session) -> None:
    db.close()