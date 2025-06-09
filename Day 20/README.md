# Mini Project - Random Quote Generator
This is a simple **Command-Line Interface (CLI)** tool that fetches a random inspirational quote from a free public API and displays it in a clean, readable format.

## What I used:
- `requests` module for making HTTP calls
- `.json()` method to parse API responses
- `try-except` block for error handling

## How it Works?
1. Sends a GET request to the Quotable API.
2. Parses the JSON response to extract the quote and the author.
3. Displays the quote in a user-friendly format.
4. Handles errors if the API is unreachable or something fails.
