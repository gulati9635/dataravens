import pandas as pd
from sqlalchemy import create_engine
import json
data = json.load(open('..\sample.json'))

df = pd.DataFrame(data["patients"])

print(df.columns)

dataframe = print(df.to_string(index=False))

# Establish connection to MySQL
engine = create_engine('mysql+pymysql://root:root123@localhost:3306/sql_db')

create_table_query = """
CREATE TABLE your_table_name (
    id INT,
    name VARCHAR(255),
    age INT
)
"""
# Load DataFrame into MySQL table
table_name = 'patients'
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Close the connection
engine.dispose()



