import requests

# Base URL of your locally hosted application
BASE_URL = "http://localhost:5000"  # Change port if different
USERS_ENDPOINT = f"{BASE_URL}/users"

def get_all_users():
    """GET request to retrieve all users"""
    try:
        response = requests.get(USERS_ENDPOINT)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        print("GET All Users Response:")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting users: {e}")

def get_single_user(user_id):
    """GET request to retrieve a single user by ID"""
    try:
        response = requests.get(f"{USERS_ENDPOINT}/{user_id}")
        response.raise_for_status()
        print(f"\nGET User {user_id} Response:")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error getting user {user_id}: {e}")

def create_user():
    """POST request to create a new user"""
    new_user = {
        "name": "Alice Wonderland",
        "email": "alice@example.com"
    }
    try:
        response = requests.post(USERS_ENDPOINT, json=new_user)
        response.raise_for_status()
        print("\nPOST Create User Response:")
        print(response.json())
        return response.json().get('id')  # Return the new user ID
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        return None

def update_user(user_id):
    """PUT request to update an existing user"""
    updated_data = {
        "name": "Updated Name",
        "email": "updated@example.com"
    }
    try:
        response = requests.put(f"{USERS_ENDPOINT}/{user_id}", json=updated_data)
        response.raise_for_status()
        print(f"\nPUT Update User {user_id} Response:")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error updating user {user_id}: {e}")

def delete_user(user_id):
    """DELETE request to remove a user"""
    try:
        response = requests.delete(f"{USERS_ENDPOINT}/{user_id}")
        response.raise_for_status()
        print(f"\nDELETE User {user_id} Response:")
        print({"status": "success", "message": f"User {user_id} deleted"})
    except requests.exceptions.RequestException as e:
        print(f"Error deleting user {user_id}: {e}")

if __name__ == "__main__":
    # Test all the API endpoints
    get_all_users()
    
    # Test creating a new user
    new_user_id = create_user()
    
    if new_user_id:
        # Test getting the new user
        get_single_user(new_user_id)
        
        # Test updating the user
        update_user(new_user_id)
        
        # Test deleting the user
        delete_user(new_user_id)
    
    # Verify the user was deleted
    get_all_users()