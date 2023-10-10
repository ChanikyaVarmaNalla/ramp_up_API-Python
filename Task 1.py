from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Read data from the JSON file
try:
    with open('books.json', 'r') as file:
        books = json.load(file)
except FileNotFoundError:
    books = []

# Save data to the JSON file
def save_data():
    with open('books.json', 'w') as file1:
        json.dump(books, file1, indent=4)

# List all books
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books)

# Get details of a specific book by its ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Add a new book to the list
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "book_name": data['book_name'],
        "author": data['author']
    }
    books.append(new_book)
    save_data()  # Save the updated data to the JSON file
    return jsonify(new_book), 201

# Update the details of an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book["book_name"] = data['book_name']
        book["author"] = data['author']
        save_data()  # Save the updated data to the JSON file
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete a book from the list
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        books.remove(book)
        save_data()  # Save the updated data to the JSON file
        return jsonify({"message": "Book deleted"})
    else:
        return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
