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
st.sidebar.write("##")
multiselect = st.sidebar.multiselect("Sélectionnez les thèmes", all_theme)

st.write("##")
st.divider()
st.write("##")

if multiselect:

    if (
        "current_theme" not in st.session_state
        or "current_card" not in st.session_state
    ):
        current_theme = random.choice(multiselect)
        card_by_themes = get_cards_by_theme(current_theme[0])

        if card_by_themes == "Aucune carte trouvé.":
            st.write(card_by_themes)
        else:
            max_proba = max([carte[3] for carte in card_by_themes])
            most_possible_card = [
                carte for carte in card_by_themes if carte[3] == max_proba
            ]
            st.session_state.current_theme = current_theme
            st.session_state.current_card = random.choice(most_possible_card)

    if "current_card" in st.session_state:
        current_theme = st.session_state.current_theme
        current_card = st.session_state.current_card

        etape_correction = st.session_state.get("etape_correction", False)

        if not etape_correction:
            with st.form("reponse_form"):
                st.markdown(
                    f"<h2 style='color: black;'>Thème: {current_theme[1]} </h2>",
                    unsafe_allow_html=True,
                )
                st.divider()

                st.text_input("Question", current_card[1], disabled=True)
                reponse = st.text_area("Votre réponse")

                submit_reponse = st.form_submit_button("Valider ma réponse")

            if submit_reponse:

                st.session_state.derniere_reponse = reponse
                st.session_state.etape_correction = True
                st.rerun()

        else:
            st.markdown(
                f"<h2 style='color: black;'>Thème: {current_theme[1]} </h2>",
                unsafe_allow_html=True,
            )
            st.divider()

            st.text_input("Question", current_card[1], disabled=True)
            st.text_area(
                "Votre réponse",
                st.session_state.get("derniere_reponse", ""),
                disabled=True,
            )
            st.text_input("Bonne réponse", current_card[2], disabled=True)

            col1, col2 = st.columns(2)
            with col1:
                bonne = st.button("J'avais bon")
            with col2:
                mauvaise = st.button("Je me suis trompé")

            if bonne or mauvaise:
                est_correcte = bonne

                update_stats(est_correcte)
                update_card_probability(current_card[0], est_correcte)

                current_theme = random.choice(multiselect)
                card_by_themes = get_cards_by_theme(current_theme[0])

                if card_by_themes == "Aucune carte trouvé.":
                    st.write(card_by_themes)
                else:
                    max_proba = max([carte[3] for carte in card_by_themes])
                    most_possible_card = [
                        carte for carte in card_by_themes if carte[3] == max_proba
                    ]
                    st.session_state.current_theme = current_theme
                    st.session_state.current_card = random.choice(most_possible_card)

                st.session_state.etape_correction = False
                st.rerun()
else:
    st.sidebar.write("Veuillez choisir un thème.")
