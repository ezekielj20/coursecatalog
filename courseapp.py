
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for personal records
entrepreneurs = []

@app.route('/persons/bulk-upload', methods=['POST'])
def bulk_upload_persons():
    try:
        data = request.get_json()
        if not data or 'persons' not in data:
            return jsonify({"error": "Invalid request format"}), 400
        
        for person in data['persons']:
            if 'person_id' not in person or 'name' not in person or 'course_id' not in person:
                return jsonify({"error": "Each entry must have 'person_id', 'name', and 'course_id'"}), 400
            if 'score' in person and (not isinstance(person['score'], (int, type(None))) or not (0 <= person['score'] <= 5)):
                return jsonify({"error": "Score must be an integer between 0 and 5, or empty"}), 400
            
            # Add to in-memory storage
            entrepreneurs.append(person)
        
        return jsonify({"message": "Entrepreneurs' data uploaded successfully", "persons": entrepreneurs}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
