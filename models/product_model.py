from sqlalchemy import Column, Integer, String, Float

from core.database import Base

class ProductModel(Base):
    __tablename__ = 'products'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255))
    price: float = Column(Float)
    description: str = Column(String(255))
    

