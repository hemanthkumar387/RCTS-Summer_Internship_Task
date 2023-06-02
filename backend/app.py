from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['Task']
collection = db['formdata']

class User:
    def __init__(self, name, age, gender, favoritesport):
        self.name = name
        self.age = age
        self.gender = gender
        self.favoritesport = favoritesport

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.get_json()

    name = data['name']
    age = data['age']
    gender = data['gender']
    favoritesport = data['favoriteSport']

    # Create a new User object
    user = User(name=name, age=age, gender=gender, favoritesport=favoritesport)

    # Save the user to the database
    collection.insert_one(user.__dict__)

    return jsonify({'message': 'Data saved successfully'})

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']  # Get the uploaded file
    df = pd.read_excel(file)  # Read the Excel file into a DataFrame

    # Connect to the MongoDB database
    client = MongoClient('mongodb://localhost:27017')
    db = client['Task']
    collection = db['exceldata']

    # Delete existing data from the collection
    collection.delete_many({})

    # Insert the data from the DataFrame into the collection
    data = df.to_dict('records')
    collection.insert_many(data)

    return 'Data uploaded successfully!'

@app.route('/formdata', methods=['GET'])
def get_formdata():
    # Connect to the MongoDB database
    client = MongoClient('mongodb://localhost:27017')
    db = client['Task']
    collection = db['formdata']

    # Retrieve all documents from the collection
    data = list(collection.find({}, {'_id': 0}))

    return jsonify(data)
@app.route('/exceldata', methods=['GET'])
def get_exceldata():
    # Connect to the MongoDB database
    client = MongoClient('mongodb://localhost:27017')
    db = client['Task']
    collection = db['exceldata']

    # Retrieve all documents from the collection
    data = list(collection.find({}, {'_id': 0}))

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

