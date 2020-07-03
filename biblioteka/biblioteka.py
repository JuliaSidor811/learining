from app import app, db
from app.models import Author, Intermediate, Book, Borrowed


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Author": Author,
        "Intermediate": Intermediate,
        "Book": Book,
        "Borrowed": Borrowed
    }
