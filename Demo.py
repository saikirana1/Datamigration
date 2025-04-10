from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Database URL
DATABASE_URL = "postgresql://postgres:root@localhost:5432/sai_coldstorage"

# 2. SQLAlchemy setup
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# 3. Table mappings

class BookingTable(Base):
    __tablename__ = 'booking_table'

    booking_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    phone_number = Column(String(15))
    email = Column(String(100))
    type_of_crop = Column(String(50))
    weight_of_crop = Column(Integer)
    from_place = Column(String(100))

    def __repr__(self):
        return (
            f"<BookingTable(booking_id={self.booking_id}, name={self.name}, "
            f"phone_number={self.phone_number}, email={self.email}, "
            f"type_of_crop={self.type_of_crop}, weight_of_crop={self.weight_of_crop}, "
            f"from_place={self.from_place})>"
        )

class Formers(Base):
    __tablename__ = 'formers'

    fid = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    name = Column(String(100))
    type_of_crop = Column(String(100))
    delivery_date = Column(Date)
    transport_date = Column(Date)
    lot_number = Column(String(50))
    rent_cost = Column(Integer)
    from_place = Column(String(100))

    def __repr__(self):
        return (
            f"<Formers(fid={self.fid}, name={self.name}, email={self.email}, "
            f"type_of_crop={self.type_of_crop}, delivery_date={self.delivery_date}, "
            f"transport_date={self.transport_date}, lot_number={self.lot_number}, "
            f"rent_cost={self.rent_cost}, from_place={self.from_place})>"
        )

class StorageDetails(Base):
    __tablename__ = 'storage_details'

    id = Column(Integer, primary_key=True)
    empty_lot_normal_temp = Column(Integer)
    empty_lot_deep_temp = Column(Integer)
    empty_lot_very_deep_temp = Column(Integer)
    total_empty = Column(Integer)

    def __repr__(self):
        return (
            f"<StorageDetails(id={self.id}, empty_lot_normal_temp={self.empty_lot_normal_temp}, "
            f"empty_lot_deep_temp={self.empty_lot_deep_temp}, "
            f"empty_lot_very_deep_temp={self.empty_lot_very_deep_temp}, "
            f"total_empty={self.total_empty})>"
        )

# 4. Fetch and print data from all tables
try:
    print("\n📦 Booking Table:")
    for row in session.query(BookingTable).all():
        print(row)

    print("\n👨‍🌾 Formers Table:")
    for row in session.query(Formers).all():
        print(row)

    print("\n❄️ Storage Details Table:")
    for row in session.query(StorageDetails).all():
        print(row)

except Exception as e:
    print("❌ Error:", e)
finally:
    session.close()
