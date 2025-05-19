from flask import jsonify

def get_user_controller(user_service):
    def handler(user_id):
        user = user_service.get_user(int(user_id))
        if user:
            return jsonify({"id": user.id, "name": user.name, "email": user.email})
        return jsonify({"error": "User not found"}), 404
    return handler
