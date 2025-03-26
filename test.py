import unittest
import json
from app import app, entrepreneurs

class EntrepreneursBulkUploadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        entrepreneurs.clear()  # Reset in-memory storage before each test

    def test_bulk_upload_success(self):
        request_data = {
            "persons": [
                {"person_id": "e123", "course_id": "c1", "name": "John Doe", "score": 5},
                {"person_id": "e124", "course_id": "c2", "name": "Jane Doe", "score": 5},
                {"person_id": "e123", "course_id": "c2", "name": "John Doe", "score": 4}
            ]
        }
        response = self.app.post('/persons/bulk-upload', data=json.dumps(request_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"], "Entrepreneurs' data uploaded successfully")
        self.assertEqual(len(response_data["persons"]), 3)

    def test_bulk_upload_invalid_format(self):
        request_data = {"invalidKey": []}  # Missing "persons" key
        response = self.app.post('/persons/bulk-upload', data=json.dumps(request_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_bulk_upload_missing_fields(self):
        request_data = {"persons": [{"person_id": "e125", "name": "Alice"}]}  # Missing "course_id"
        response = self.app.post('/persons/bulk-upload', data=json.dumps(request_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_bulk_upload_invalid_score(self):
        request_data = {
            "persons": [
                {"person_id": "e126", "course_id": "c3", "name": "Bob", "score": 6}  # Invalid score
            ]
        }
        response = self.app.post('/persons/bulk-upload', data=json.dumps(request_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()


