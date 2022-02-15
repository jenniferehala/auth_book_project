from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.author import Author
from flask_app.models.book import Book

# *************************************
#    Main Page / Dashboard
# *************************************


@app.route("/books")
def books():
    all_books = Book.get_books_with_authors()
    return render_template("books.html", all_books=all_books)

# *************************************
#    Create Book Routes
# *************************************


@app.route("/books/new")
def new_book():
    authors = Author.get_all_authors()
    return render_template("new_book.html", authors=authors)


@app.route("/create_book", methods=["POST"])
def create_book():
    data = {
        "title": request.form["title"],
        "genre": request.form["genre"],
        "year": request.form["year"],
        "author_id": request.form["author_id"],
        "description": request.form["description"]
    }
    Book.create_book(data)

    return redirect("/books")

# *************************************
#    Edit Book Route
# *************************************


@app.route("/books/<int:book_id>/edit")
def edit_book(book_id):
    authors = Author.get_all_authors()
    data = {
        "book_id": book_id
    }
    book = Book.get_one_book(data)
    return render_template("edit_book.html", authors=authors, book=book)


@app.route("/update_book/<int:book_id>", methods=["POST"])
def update_book(book_id):
    data = {
        "book_id": book_id,
        "title": request.form["title"],
        "genre": request.form["genre"],
        "year": request.form["year"],
        "author_id": request.form["author_id"],
        "description": request.form["description"]
    }
    Book.update_book_info(data)
    return redirect(f"/books/{book_id}")


# *************************************
#    Show  One Book Route
# *************************************


@app.route("/books/<int:book_id>")
def show_book(book_id):
    data = {
        "book_id": book_id
    }

    book = Book.get_one_book(data)
    return render_template("show_book.html", book=book)

# *************************************
#    Delete One Book Route
# *************************************


@app.route("/books/<int:book_id>/delete")
def delete_book(book_id):
    data = {
        "book_id": book_id
    }
    Book.delete_one_book(data)
    return redirect("/books")
