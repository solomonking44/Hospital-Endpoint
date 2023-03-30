import requests



BASE_URL = "http://localhost:5000"

response = requests.get(BASE_URL + "/category")

print("Test passed")
print(response.json())


