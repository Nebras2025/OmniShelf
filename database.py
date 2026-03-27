# importing important libary & their functions
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

# creating a link of database
DATABASE_URL = "sqlite:///book.db"

# connecting to my databse
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

# creating the database
Base.metadata.create_all(engine)

# reading the CSV file & store it into my database
df = pd.read_csv("final_cleaned_data.csv")
df.to_sql("book", con=engine, if_exists="replace", index=False)

