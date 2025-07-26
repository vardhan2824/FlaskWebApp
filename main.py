from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data store (simulates a database)
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

# Helper function to find item by ID
def find_item(item_id):
    return next((item for item in items if item["id"] == item_id), None)

# GET all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# GET single item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = find_item(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# POST - Create new item
@app.route('/api/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        abort(400, description="Missing 'name' in request JSON")
    new_id = items[-1]['id'] + 1 if items else 1
    new_item = {
        "id": new_id,
        "name": request.json['name']
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT - Update item
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    if not request.json or 'name' not in request.json:
        abort(400, description="Missing 'name' in request JSON")
    item['name'] = request.json['name']
    return jsonify(item), 200

# DELETE - Remove item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    items.remove(item)
    return jsonify({"message": f"Item {item_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
