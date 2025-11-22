import requests
import json

# URL for the PUT request
url = "http://localhost:8888/publishers/692162cbb298f74270f6504b/books/692162cbb298f74270f6504c"

# Data to be sent in the body of the request
data = {
    "title": "New Book Title",   # Replace with the updated title
    "author": "New Author Name", # Replace with the updated author
    "genre": "New Genre",        # Replace with the updated genre
}

# Send the PUT request
response = requests.put(url, json=data)