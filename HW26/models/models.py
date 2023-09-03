from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class AddressModel(Base):
    __tablename__ = 'addresses'
    address_id = Column(INTEGER, primary_key=True)
    city = Column(VARCHAR(100))
    country = Column(VARCHAR(100))
    customers = relationship("CustomerModel", back_populates='address')

    def __str__(self):
        return f"Id: {self.address_id}, City: {self.city}, Country: {self.country}, users - {self.users}"

    def __repr__(self):
        return f"Id - {self.address_id} City - {self.city} Country - {self.country}, users - {self.users}"


class CustomerModel(Base):
    __tablename__ = "customers"
    id = Column(INTEGER, primary_key=True)
    age = Column(INTEGER)
    name = Column(VARCHAR(100))
    address_id = Column(ForeignKey("addresses.address_id"))
    address = relationship("AddressModel", back_populates="customers")

    def __repr__(self):
        return f"Id - {self.id} Age - {self.age} Name - {self.name}, city - {self.address.city}"
