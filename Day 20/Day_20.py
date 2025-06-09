# Day 20: Mini Project - Random Quote Generator

import requests

def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            quote = data['content']
            author = data['author']
            return quote, author
        else:
            print("Failed to fetch quote. Status code:", response.status_code)
            return None, None
    except Exception as e:
        print("An error occurred:", e)
        return None, None

# Using the function
quote, author = get_random_quote()
if quote:
    print("\nHere's your quote of the moment:\n")
    print(f"\"{quote}\"")
    print(f"\n   — {author}\n")
else:
    print("Could not get a quote at the moment.")
