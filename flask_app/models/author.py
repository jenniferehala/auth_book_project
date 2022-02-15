from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


class Author:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.books = []

    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        results = connectToMySQL("authorsmodel_schema").query_db(query, data)
        return results

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL("authorsmodel_schema").query_db(query)
        authors = []
        for one_auth in results:
            authors.append(cls(one_auth))
        return authors

    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM authors LEFT JOIN books ON author_id = authors.id WHERE authors.id = %(author_id)s;"
        results = connectToMySQL("authorsmodel_schema").query_db(query, data)

        author = cls(results[0])

        for row in results:
            book_data = {
                "id": row['books.id'],
                "title": row['title'],
                "genre": row['genre'],
                "year": row['year'],
                "description": row['description'],
                "author_id": row['author_id'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at'],
            }

            author.books.append(book.Book(book_data))

        return author
