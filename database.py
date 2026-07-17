import sqlite3
from config import DATABASE

def initialiser():
    connexion = sqlite3.connect(DATABASE)
    curseur = connexion.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS historique (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            multiplicateur REAL NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connexion.commit()
    connexion.close()


def ajouter_resultat(valeur):
    connexion = sqlite3.connect(DATABASE)
    curseur = connexion.cursor()

    curseur.execute(
        "INSERT INTO historique (multiplicateur) VALUES (?)",
        (valeur,)
    )

    connexion.commit()
    connexion.close()


def lire_historique():
    connexion = sqlite3.connect(DATABASE)
    curseur = connexion.cursor()

    curseur.execute(
        "SELECT multiplicateur FROM historique ORDER BY id"
    )

    donnees = [ligne[0] for ligne in curseur.fetchall()]

    connexion.close()

    return donnees
