from flask import Flask, request, jsonify
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://yossr:{password}@cluster0.8bpprbf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

login_db = client.Login
collections = login_db.authentication

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    # Vérifier les informations d'identification dans la base de données MongoDB
    user = collections.find_one({'email': email, 'password': password})
    
    if user:
        # L'utilisateur est authentifié avec succès
        return jsonify({'message': 'Connexion réussie !'})
    else:
        # L'utilisateur n'existe pas ou le mot de passe est incorrect
        return jsonify({'message': 'Nom d\'utilisateur ou mot de passe incorrect'}), 401

if __name__ == '__main__':
    app.run(debug=True)
