from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


Base = declarative_base() # factory

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))

    def __str__(self):
        return self.name.upper()


class Balance(Base):
    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)

    person_id = Column(Integer, ForeignKey(Person.id))

    person = relationship("Person", foreign_keys="Balance.person_id")

engine = create_engine("sqlite:///database.db")

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

# person = Person(name="Guido")
# session.add(person) # INSERT INTO PERSON (NAME) values ('GUIDO');

# person = Person(name="Maria")
# session.add(person)

# session.commit()


# results = session.query(Person)

# for result in results:
#     balance = Balance(value=40,  person_id=result.id)
#     session.add(balance)

# session.commit()

# results = session.query(Balance)
# for result in results:
#     print(result.value, result.person)


results = session.query(Person.name, Balance.value).join(Balance, isouter=True)
for result in results:
    print(result)
