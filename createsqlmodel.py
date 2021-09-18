from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


#def create_db_and_tables():
    #SQLModel.metadata.create_all(engine)


#if __name__ == "__main__":
    #create_db_and_tables()
#
#create rows

hero_1 = Hero(name="Deadpool", secret_name="Ryan Reynolds")
hero_2 = Hero(name="Chandler Bing", secret_name="Matthew Perry")
hero_3 = Hero(name="Monica Geller", secret_name="Courtney Cox", age=48)


# write to database

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

#with Session(engine) as session:
    #session.add(hero_1)
    #session.add(hero_2)
    #session.add(hero_3)
    #session.commit()

# Read Data with SQLModel
# Create a Session

def select_heroes():

    with Session(engine) as session:
        statement = select(Hero)
        results = session.exec(statement)
        for hero in results:
            print(hero)

# To print on cmd
def main():
    #create_db_and_tables()
    #create_heroes()
    select_heroes()


if __name__ == "__main__":
    main()





