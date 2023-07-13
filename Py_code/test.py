import json
json_data = '''
[
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25}
]
'''
data = json.loads(json_data)

cursor = connection.cursor()

# Insert data into the MySQL table
for item in data:
    insert_query = """
    INSERT INTO your_table (id, name, age)
    VALUES (%s, %s, %s)  
    """
    values = (item['id'], item['name'], item['age'])
    cursor.execute(insert_query, values)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()


