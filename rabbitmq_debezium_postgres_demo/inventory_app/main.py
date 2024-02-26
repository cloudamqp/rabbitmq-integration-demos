import time

from database.models import Base
from database.conn import engine, db, close_conn
from database.crud import add_product


def generate_product(i: int) -> dict:
    return {"name": f"product-{i}", "quantity": i}


def add_products() -> None:
    counter: int = 0

    # Add 500 products: 5 secs interval
    while counter < 500:
        product: dict = generate_product(counter)
        add_product(db=db, product=product)
        print(f"product-{counter} inserted")
        time.sleep(5)
        counter += 1


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    add_products()
    close_conn(db=db)