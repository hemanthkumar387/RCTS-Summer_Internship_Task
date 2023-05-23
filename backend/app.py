from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017')
db = client['Task']
collection = db['formdata']

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.get_json()
    formatted_data = {}
    for entry in data:
        formatted_data[entry['question']] = entry['answer']
    collection.insert_one(formatted_data)
    return jsonify({'message': 'Data saved successfully'})
if __name__ == '__main__':
    app.run(debug=True)






