import streamlit as st
from projet_flashcards import init_db, get_all_themes, get_number_of_cards
import os

st.set_page_config(
    page_title="Application de flashcard", page_icon=":house:", layout="wide"
)

if not os.path.exists("flashcards.db"):
    init_db()

all_theme = get_all_themes()

if all_theme:
    current_theme = all_theme[0]
    st.sidebar.write(f"Nombre de carte total : {get_number_of_cards()}")
else:
    st.sidebar.write(f"Nombre de carte total : 0")
