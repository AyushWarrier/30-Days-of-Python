# Day 25: Building a Basic API

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"},
]

@app.route("/")
def home():
    return "📘 Welcome to the Book API!"

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
