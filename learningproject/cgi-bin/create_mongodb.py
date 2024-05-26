from pymongo import MongoClient

# Connect to the MongoDB server (default host and port)
client = MongoClient('localhost', 27017)

# Create a new database called "mydatabase"
db = client['mydatabase']

# Create a new collection called "students"
collection = db['students']

# Create a document to insert into the collection
student_document = {
    'student_id': 'GITAM123',
    'name': 'John Doe',
    'password': 'password123',
    'attendance_percentage': 95,
    'number_of_camps_attended': 5,
    'marks_B_certificate_exam': 80,
    'marks_C_certificate_exam': 85,
    'position_among_competitors': 1
}

# Insert the document into the collection
inserted_id = collection.insert_one(student_document).inserted_id

# Print the ID of the inserted document
print(f'Document inserted with ID: {inserted_id}')

# Verify the document was inserted by retrieving it
retrieved_document = collection.find_one({'student_id': 'GITAM123'})
print('Retrieved Document:', retrieved_document)
