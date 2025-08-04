Python Web Application that is capable of responding the multiple API  request when hosted from the local machine 

GET – Retrieves data from the API, such as listing all items or getting a specific item (e.g., http://localhost:5000/api/items).

POST – Sends data to the API to create a new item in the system (e.g., http://localhost:5000/api/items with a JSON body).

PUT – Updates an existing item by sending new data to a specific endpoint (e.g., http://localhost:5000/api/items/2).

DELETE – Removes a specific item from the API’s data store (e.g., http://localhost:5000/api/items/2).


API's endpoints :
Method	Endpoint	Action
GET	/users	Get all users
GET	/users/<id>	Get a specific user by ID
POST	/users	Create a new user
PUT	/users/<id>	Update a user by ID
DELETE	/users/<id>	Delete a user by ID
