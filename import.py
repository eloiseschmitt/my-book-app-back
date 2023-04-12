import json

from config import app
from model import db, Book

# Ouvrir le fichier JSON et lire les données
with open('books.json') as f:
    data = json.load(f)

# Itérer sur les données et créer une instance du modèle de données SQLAlchemy pour chaque entrée
for item in data:
    book = Book(title=item['title'], author=item['author'], read=item['read'])

    # Ajouter chaque instance du modèle de données à la session SQLAlchemy et commiter les modifications
    with app.app_context():
        db.session.add(book)
        db.session.commit()
