from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

def insert_student_document():
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    collection = db['students']

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

    inserted_id = collection.insert_one(student_document).inserted_id
    print("Data Inserted 12....")
    retrieved_document = collection.find_one({'student_id': 'GITAM123'})
    return retrieved_document

@app.route('/insert_student', methods=['GET'])
def insert_student():
    document = insert_student_document()
    return jsonify({
        'student_id': document['student_id'],
        'name': document['name'],
        'attendance_percentage': document['attendance_percentage'],
        'number_of_camps_attended': document['number_of_camps_attended'],
        'marks_B_certificate_exam': document['marks_B_certificate_exam'],
        'marks_C_certificate_exam': document['marks_C_certificate_exam'],
        'position_among_competitors': document['position_among_competitors']
    })

if __name__ == '__main__':
    app.run(debug=True)
