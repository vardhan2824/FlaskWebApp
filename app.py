from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Dummy user data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com"}
]

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        # Return all users with 200 OK
        return jsonify({"users": users}), 200
    
    elif request.method == 'POST':
        if not request.json or 'name' not in request.json or 'email' not in request.json:
            # Return 400 Bad Request if data is incomplete
            abort(400)
        
        # Create new user
        new_user = {
            "id": len(users) + 1,
            "name": request.json['name'],
            "email": request.json['email']
        }
        users.append(new_user)
        
        # Return 201 Created with the new user
        return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        # Return 404 Not Found if user doesn't exist
        abort(404)
    # Return 200 OK with the user data
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)  # User not found
    
    if not request.json:
        abort(400)  # Bad request (no data provided)
    
    # Update user data (only if fields are provided)
    if 'name' in request.json:
        user['name'] = request.json['name']
    if 'email' in request.json:
        user['email'] = request.json['email']
    
    return jsonify(user), 200
    
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)  # User not found
    
    users.remove(user)
    return jsonify({"message": "User deleted successfully"}), 200

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": "Name and email are required"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)