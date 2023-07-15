import pandas as pd
from sqlalchemy import create_engine
import json
data = json.load(open('..\sample.json'))

df = pd.DataFrame(data["patients"])

print(df.columns)

dataframe = print(df.to_string(index=False))

# Establish connection to MySQL
engine = create_engine('mysql+pymysql://root:root123@localhost:3306/sql_db')
# Load DataFrame into MySQL table
engine.dispose()

table_name = 'patients'
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Close the connection



