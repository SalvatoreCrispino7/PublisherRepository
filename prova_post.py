import subprocess
import json
import time

def test_create_publisher():
    publisher_data = {
        "name": "New Publisher",
        "founded_year": 1990,
        "country": "USA"
    }

    result = subprocess.run(
        [
            "curl", "-X", "POST", "http://localhost:8888/publishers",
            "-H", "Content-Type: application/json",
            "-d", json.dumps(publisher_data)
        ],
        capture_output=True, text=True
    )
    print("POST /publishers result:")
    print(result.stdout)

def test_get_publishers():
    result = subprocess.run(
        ["curl", "http://localhost:8888/publishers"],
        capture_output=True, text=True
    )
    print("GET /publishers result:")
    print(result.stdout)

def test_create_book():
    book_data = {
        "title": "New Book Title",
        "author": "Author Name",
        "genre": "Fiction"
    }

    result = subprocess.run(
        [
            "curl", "-X", "POST", "http://localhost:8888/publishers/692162cbb298f74270f6504b/books",  # Replace with an actual publisher id
            "-H", "Content-Type: application/json",
            "-d", json.dumps(book_data)
        ],
        capture_output=True, text=True
    )
    print("POST /publishers/{id}/books result:")
    print(result.stdout)

def test_get_books_by_publisher():
    result = subprocess.run(
        ["curl", "http://localhost:8888/publishers/692162cbb298f74270f6504b/books"],  # Replace with an actual publisher id
        capture_output=True, text=True
    )
    print("GET /publishers/{id}/books result:")
    print(result.stdout)

def test_update_book():
    book_update_data = {
        "title": "Updated Book Title",
        "author": "Updated Author Name",
        "genre": "Updated Genre"
    }

    result = subprocess.run(
        [
            "curl", "-X", "PUT", "http://localhost:8888/publishers/692162cbb298f74270f6504b/books/692162cbb298f74270f6504c",  # Replace with actual publisher & book id
            "-H", "Content-Type: application/json",
            "-d", json.dumps(book_update_data)
        ],
        capture_output=True, text=True
    )
    print("PUT /publishers/{id}/books/{id} result:")
    print(result.stdout)

def test_delete_book():
    result = subprocess.run(
        [
            "curl", "-X", "DELETE", "http://localhost:8888/publishers/692162cbb298f74270f6504b/books/692162cbb298f74270f6504c",  # Replace with actual publisher & book id
        ],
        capture_output=True, text=True
    )
    print("DELETE /publishers/{id}/books/{id} result:")
    print(result.stdout)

def test_update_publisher():
    publisher_update_data = {
        "name": "Updated Publisher",
        "founded_year": 1995,
        "country": "Canada"
    }

    result = subprocess.run(
        [
            "curl", "-X", "PUT", "http://localhost:8888/publishers/692162cbb298f74270f6504b",  # Replace with an actual publisher id
            "-H", "Content-Type: application/json",
            "-d", json.dumps(publisher_update_data)
        ],
        capture_output=True, text=True
    )
    print("PUT /publishers/{id} result:")
    print(result.stdout)

def test_delete_publisher():
    result = subprocess.run(
        [
            "curl", "-X", "DELETE", "http://localhost:8888/publishers/692162cbb298f74270f6504b",  # Replace with an actual publisher id
        ],
        capture_output=True, text=True
    )
    print("DELETE /publishers/{id} result:")
    print(result.stdout)

def main():

    print("\n--- Running tests ---\n")
    test_create_publisher()
    test_get_publishers()
    test_create_book()
    test_get_books_by_publisher()
    test_update_book()
    test_delete_book()
    test_update_publisher()
    test_delete_publisher()

if __name__ == "__main__":
    main()
