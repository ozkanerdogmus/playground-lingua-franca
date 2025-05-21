import requests
import json
import os

# Get the external URL
external_url = "https://work-1-oennpdgcnhktvura.prod-runtime.all-hands.dev"

# Send a request to the server
response = requests.post(
    f"{external_url}/addone",
    json={"data": 42}
)

# Print the response
print("Response status code:", response.status_code)
print("Response content:", response.json())