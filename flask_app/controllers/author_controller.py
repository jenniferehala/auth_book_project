from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.author import Author


# *************************************
# Create Author Route
# *************************************

@app.route("/new_author", methods=["POST"])
def new_author():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"]
    }
    Author.create_author(data)
    return redirect("/books")

# *************************************
# Create One Author Route
# *************************************


@app.route("/author/<int:author_id>")
def show_author(author_id):
    data = {
        "author_id": author_id
    }

    author = Author.get_one_author(data)
    return render_template("show_author.html", author=author)
