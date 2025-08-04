import requests
import pandas as pd
response = requests.get('http://localhost:5000/users')
data = response.json()
print(pd.DataFrame(data['users']))