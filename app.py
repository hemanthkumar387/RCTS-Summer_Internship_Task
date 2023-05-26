from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/save-data": {"origins": "http://localhost:3000"}})

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['Task']
collection = db['formdata']

class User:
    def __init__(self, name, age, gender, favorite_sport):
        self.name = name
        self.age = age
        self.gender = gender
        self.favorite_sport = favorite_sport

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.get_json()

    name = data['name']
    age = data['age']
    gender = data['gender']
    favorite_sport = data['favoriteSport']

    # Create a new User object
    user = User(name=name, age=age, gender=gender, favorite_sport=favorite_sport)

    # Save the user to the database
    collection.insert_one(user.__dict__)

    return jsonify({'message': 'Data saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)











# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from pymongo import MongoClient
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# client = MongoClient('mongodb://localhost:27017')
# db = client['Task']
# collection = db['exceldata']

# @app.route('/upload-excel', methods=['POST'])
# def upload_excel():
#     file = request.files['file']
#     df = pd.read_excel(file)

#     data = df.to_dict(orient='records')
#     collection.insert_many(data)

#     return jsonify({'message': 'Excel data uploaded successfully'})

# @app.route('/get-data', methods=['GET'])
# def get_data():
#     data = list(collection.find({}, {'_id': 0}))
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)
