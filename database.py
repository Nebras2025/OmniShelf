# importing important libary & their functions
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

# creating a link of database
DATABASE_URL = "sqlite:///books.db"

# connecting to my databse
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

# creating the database
Base.metadata.create_all(engine)

# reading the CSV file & store it into my database
df = pd.read_csv("cleaned_data.csv")
df.to_sql("books", con=engine, if_exists="replace", index=False)

