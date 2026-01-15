import pandas as pd
from sqlalchemy import create_engine

# CSV file path
csv_file = "players.csv"

# MySQL connection details
user = "root"
password = "root"
host = "localhost"
port = 3307
database = "basketball_db"
table_name = "players"

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
)

# Load CSV into DataFrame
df = pd.read_csv(csv_file)

# Insert into MySQL
df.to_sql(
    name=table_name,
    con=engine,
    if_exists="append",  # 'replace' to drop & recreate table
    index=False
)

print("CSV data loaded successfully!")
