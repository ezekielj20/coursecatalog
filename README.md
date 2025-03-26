# coursecatalog

How to run the api
1. Install dependencies
    ##
        pip install flask

2. Run the API
   ##
        python courseapp.py

3  Can use CURL or Postman orpython's request to send a get request to
   ##
        http://127.0.0.1:5000/persons/progress/e123

4. How to run tests
   ##
        sh
        python test.py

Request for GET (GET /persons/progress/e123)
##
    curl -X GET "http://127.0.0.1:5000/progress/e123"
Response
##  
    json
    {
    "person_id": "e123",
    "name": "John Doe",
    "courses_taken": ["Accounting 101", "Marketing 101"],
    "gpa": 4.5
    }


Request for POST (POST /persons/bulk-upload)
##
    json
     {
    "persons": [
        {"person_id": "e123", "course_id": "c1", "name": "John Doe", "score": 5},
        {"person_id": "e124", "course_id": "c2", "name": "Jane Doe", "score": 5},
        {"person_id": "e123", "course_id": "c2", "name": "John Doe", "score": 4}
    ]
    }
Response for POST
##
    json
    {
    "message": "Entrepreneurs' data uploaded successfully",
    "persons": [
        {"person_id": "e123", "course_id": "c1", "name": "John Doe", "score": 5},
        {"person_id": "e124", "course_id": "c2", "name": "Jane Doe", "score": 5},
        {"person_id": "e123", "course_id": "c2", "name": "John Doe", "score": 4}
    ]
    }
