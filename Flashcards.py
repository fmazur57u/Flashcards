import streamlit as st
from projet_flashcards import *
import os
import random

st.set_page_config(page_title="Flashcards", layout="wide", page_icon=":house:")

st.markdown(
    "<h1 style='text-align: center; color: black;'>Application de flashcards </h1>",
    unsafe_allow_html=True,
)
if not os.path.exists("flashcards.db"):
    init_db()

all_theme = get_all_themes()

st.sidebar.write(f"Nombre de carte total : {get_number_of_cards()}")
st.write("##")
st.divider()
st.write("##")

current_theme = random.choice(all_theme)
card_by_themes = get_cards_by_theme(current_theme[0])
if card_by_themes != "Aucune carte trouvé.":
    with st.form("my_form"):
        st.markdown(
            f"<h2 color: black;'>Thème: {current_theme[1]} </h2>",
            unsafe_allow_html=True,
        )

        st.divider()
        max_proba = max([carte[3] for carte in card_by_themes])
        most_possible_card = [
            carte for carte in card_by_themes if carte[3] == max_proba
        ]
        current_card = random.choice(most_possible_card)
        text_input = st.text_input("Question", current_card[1])
        text_area = st.text_area("Votre réponse")
        submit_button = st.form_submit_button("submit")
else:
    st.write(card_by_themes)
