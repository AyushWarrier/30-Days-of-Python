# Day 18: Working with APIs

'''
Today, I start learning how to work with APIs (Application Programming Interfaces) in Python.
For example, using an API, you can fetch weather data, news, or even GitHub info using an API.
Most APIs return data in **JSON** format, which is like a dictionary in Python.
'''

# We'll use the `requests` module to make HTTP requests to APIs
import requests

# Example: Using a public API (https://api.agify.io)
'''
This API predicts age based on a name.
'''

name = "Ayush"
url = f"https://api.agify.io/?name={name}"

# Making the GET request
response = requests.get(url)

# Check if request was successful 
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dict
    print(f"Name: {data['name']}")
    print(f"Predicted Age: {data['age']}")
    print(f"Count: {data['count']}")
else:
    print("Failed to retrieve data from API")

'''
📌 Notes:
- `.get()` method from requests is used to fetch data.
- `.json()` converts the API response into a Python dictionary.
- We always check if the status code is 200 before using the data.
There are many APIs online, and some need API keys (like Weather, YouTube, etc.)
'''

# Another fun public API I tried: Bored API (https://www.boredapi.com/api/activity)
print("\nUsing Bored API to suggest an activity...")

activity_url = "https://www.boredapi.com/api/activity"
activity_response = requests.get(activity_url)

if activity_response.status_code == 200:
    activity_data = activity_response.json()
    print("Suggestion:", activity_data["activity"])
else:
    print("Could not fetch activity")
