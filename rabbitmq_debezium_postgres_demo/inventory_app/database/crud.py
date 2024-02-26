from sqlalchemy.orm import Session

from .models import Product


def get_product_by_id(db: Session, id: int) -> Product:
    return db.query(Product).filter(Product.id == id).first()


def add_product(db: Session, product: dict) -> Product:
    product: Product = Product(name=product["name"], quantity=product["quantity"])
    db.add(product)
    db.commit()
    db.refresh(product)
    return product