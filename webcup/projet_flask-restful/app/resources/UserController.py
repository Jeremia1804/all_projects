from flask import Flask, request
from flask_restful import Api, Resource


# Simuler une base de données d'utilisateurs
users = {
    1: {"id": 1, "name": "John Doe", "age": 30},
    2: {"id": 2, "name": "Jane Smith", "age": 25}
}

class UserResource(Resource):
    def get(self, user_id = None):
        if user_id is None:
            return users, 200
        if user_id in users:
            return users[user_id], 200
        else:
            return {"message": "Utilisateur non trouvé"}, 404
    
    def get_all(self):
        return users, 200

    def post(self):
        data = request.json
        user_id = max(users.keys()) + 1
        data['id'] = user_id
        users[user_id] = data
        return {"message": "Utilisateur ajouté avec succès", "user": data}, 201

    def put(self, user_id):
        if user_id in users:
            data = request.json
            users[user_id].update(data)
            return {"message": "Utilisateur mis à jour avec succès", "user": users[user_id]}, 200
        else:
            return {"message": "Utilisateur non trouvé"}, 404

    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return {"message": "Utilisateur supprimé avec succès"}, 200
        else:
            return {"message": "Utilisateur non trouvé"}, 404

