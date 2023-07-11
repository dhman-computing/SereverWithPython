# Doesn't work

from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Access a database
db = client['your_database']

# Access a collection
collection = db['your_collection']

# Prepare a document to insert
document = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com'
}

# Insert the document into the collection
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)


# Close the connection
client.close()