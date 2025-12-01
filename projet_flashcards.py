import sqlite3
from datetime import datetime
import os
import streamlit as st


# Fonction pour initialiser la base de données
def init_db():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute(
        """CREATE TABLE IF NOT EXISTS cards(
            id INTEGER PRIMARY KEY,
            question TEXT,
            reponse TEXT,
            probabilite REAL CHECK (probabilite >= 0.1 AND probabilite <= 1),
            id_theme INTEGER,
            FOREIGN KEY (id_theme) REFERENCES themes(id) ON DELETE RESTRICT);"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS themes(
            id INTEGER PRIMARY KEY,
            theme TEXT);"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS stats(
            id INTEGER PRIMARY KEY,
            bonnes_reponses INTEGER,
            mauvaises_reponses INTEGER,
            date TEXT);
            """
    )
    c.execute(
        """INSERT INTO themes (id, theme) VALUES 
              (1, 'Prise en main de la machine'),
              (2, 'Python'),
              (3, 'SQL'),
              (4, 'Git'),
              (5, 'La méthodologie du data scientist');"""
    )
    conn.commit()
    conn.close()


# Fonctions pour le CRUD de cards


def create_card(question, reponse, probabilite, id_theme):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute(
        """INSERT INTO cards (question, reponse, probabilite, id_theme)
              VALUES (?, ?, ?, ?)""",
        (question, reponse, probabilite, id_theme),
    )
    conn.commit()
    conn.close()


"""
create_card(
    "Comment reconnaître un probléme de régréssion ou de classification?",
    "Régréssion = Target continue, Classification = Target discret.",
    0.1,
    4,
)
"""


# Fonction pour récupérer une carte selon l'id
def get_card(id):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""SELECT * FROM cards WHERE id = ? """, (id,))
    carte = c.fetchone()
    conn.close()
    if carte:
        return carte
    else:
        return "Aucune carte trouvé."


"""
print(get_card(1))
print(get_card(2))
"""


# Mettre à jour des informations d'une carte
def update_card(id, question, reponse, probabilite, id_theme):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute(
        """UPDATE cards set question = ?, reponse = ?, probabilite = ?, id_theme = ?
              WHERE id = ?""",
        (question, reponse, probabilite, id_theme, id),
    )
    conn.commit()
    conn.close()


"""
update_card(
    1, "Que veut dire SCF?", "Self-consistent-field (champ auto-cohérent)", 0.1, 1
)
"""


# Supprimer carte
def delete_cards(id):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""DELETE FROM cards WHERE id = ?""", (id,))
    conn.commit()
    conn.close()


# Récupérer toutes les cartes
def get_all_cards():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""SELECT * FROM cards""")
    cartes = c.fetchall()
    conn.close()
    return cartes


# print(get_all_cards())


# Fonction pour avoir le nombre de carte.
def get_number_of_cards():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""SELECT COUNT(*) FROM cards""")
    nombre_cartes = c.fetchone()
    conn.close()
    return nombre_cartes[0]


# print(get_number_of_cards())


def get_cards_by_theme(id_theme):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""SELECT * FROM cards WHERE id_theme = ? """, (id_theme,))
    cartes = c.fetchall()
    conn.close()
    if cartes:
        return cartes
    else:
        return "Aucune carte trouvé."


"""
print(get_cards_by_theme(1))
print(get_cards_by_theme(4))
print(get_cards_by_theme(2))
"""

# Fonctions pour le CRUD de themes


# Créer un théme
def create_theme(theme):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute(
        """INSERT INTO themes (theme)
              VALUES (?)""",
        (theme,),
    )
    conn.commit()
    conn.close()


# create_theme("Application de la data science en chimie")


# Obtenir un théme selon l'id
def get_theme(id):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""SELECT * FROM themes WHERE id = ? """, (id,))
    theme = c.fetchone()
    conn.close()
    if theme:
        return theme
    else:
        return "Aucun théme trouvé."


"""
print(get_theme(1))
print(get_theme(20))
"""


# Mettre à jour des informations d'un théme
def update_theme(id, theme):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""UPDATE themes set theme = ? WHERE id = ?""", (theme, id))
    conn.commit()
    conn.close()


# update_theme(6, "Application du machine learning en chimie.")


# Supprimer un théme
def delete_theme(id):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""DELETE FROM themes WHERE id = ?""", (id,))
    conn.commit()
    conn.close()


# delete_theme(6)


# Récupérer toutes les cartes
def get_all_themes():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""SELECT * FROM themes""")
    themes = c.fetchall()
    conn.close()
    return themes


# print(get_all_themes())

# Fonctions pour les statistiques


# Mettre à jour les statistiques
def update_stats(is_correct):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        c.execute(
            "SELECT id, bonnes_reponses, mauvaises_reponses FROM stats WHERE date = ?",
            (today,),
        )
    except Exception as e:
        print("Exception: {}".format(e))
        raise Exception(e)
    stats = c.fetchone()
    if stats:
        id, bonnes_reponses, mauvaises_reponses = stats
        if is_correct:
            bonnes_reponses += 1
        else:
            mauvaises_reponses += 1
        try:
            c.execute(
                """
                UPDATE stats
                SET bonnes_reponses = ?, mauvaises_reponses=?
                WHERE id = ?
                """,
                (bonnes_reponses, mauvaises_reponses, id),
            )
        except Exception as e:
            print("Exception: {}".format(e))
            raise Exception(e)
    else:
        bonnes_reponses = 1 if is_correct else 0
        mauvaises_reponses = 0 if is_correct else 1
        try:
            c.execute(
                """
                    INSERT INTO stats (bonnes_reponses, mauvaises_reponses, date)
                    VALUES (?, ?, ?)
                    """,
                (bonnes_reponses, mauvaises_reponses, today),
            )
        except Exception as e:
            print("Exception: {}".format(e))
            raise Exception(e)
    conn.commit()
    conn.close()


# update_stats(False)


# Mettre à jour les probabilités des cartes
def update_card_probability(card_id, is_correct):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    try:
        c.execute("SELECT probabilite FROM cards WHERE id = ?", (card_id,))
    except Exception as e:
        print("Exception: {}".format(e))
        raise Exception(e)
    probabilite = c.fetchone()
    if probabilite:
        probabilite = probabilite[0]
        if is_correct == True:
            probabilite *= 0.9
        else:
            probabilite *= 1.1
        if probabilite < 0.1 or probabilite > 1:
            probabilite = max(0.1, min(probabilite, 1))
        try:
            c.execute(
                "UPDATE cards SET probabilite = ? WHERE id = ?", (probabilite, card_id)
            )
        except Exception as e:
            print("Exception: {}".format(e))
            raise Exception(e)
    else:
        print("Aucune carte à été trouvé.")
    conn.commit()
    conn.close()


# update_card_probability(2, True)


# Obtenir toutes les statistiques à travers le temps
def get_stats():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("SELECT bonnes_reponses, mauvaises_reponses, date FROM stats")
    stats = c.fetchall()
    conn.close()
    return stats


# print(get_stats())
