import streamlit as st
from projet_flashcards import *

st.set_page_config(page_title="Configuration", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: black;'>Configuration </h1>",
    unsafe_allow_html=True,
)
st.write("##")
st.write("##")
with st.form("ajouter_theme"):
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Ajouter des thèmes </h1>",
        unsafe_allow_html=True,
    )
    theme_a_ajouter = st.text_input("Nom du thème à ajouter")
    ajouter_theme = st.form_submit_button("Ajouter le thème")
    if ajouter_theme:
        create_theme(theme_a_ajouter)
        st.write(f"Le thème {theme_a_ajouter[1]} à bien été ajouter.")

st.write("##")
st.write("##")

with st.form("supprimer_theme"):
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Supprimer des thèmes </h1>",
        unsafe_allow_html=True,
    )
    theme_a_supprimer = st.selectbox(
        "Sélectionnez un thème à supprimer", get_all_themes()
    )
    supprimer_theme = st.form_submit_button("Supprimer le thème")
    if supprimer_theme:
        delete_theme(theme_a_supprimer[0])
        st.write(f"Le thème {theme_a_supprimer[1]} à bien été supprimer.")

st.write("##")
st.write("##")

with st.form("update_theme"):
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Mettre à jour des thèmes </h1>",
        unsafe_allow_html=True,
    )
    theme_a_update = st.selectbox(
        "Sélectionnez un thème à mettre à jour", get_all_themes()
    )
    nouveau_theme = st.text_area("Nouveau nom du thème")
    updated_theme = st.form_submit_button("Mettre à jour le thème")
    if updated_theme:
        update_theme(theme_a_update[0], nouveau_theme)
        st.write(f"Le thème {theme_a_update[1]} à bien été mis à jour.")

st.write("##")
st.write("##")

with st.form("ajouter_flashcards"):
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Ajouter une nouvelle flashcard </h1>",
        unsafe_allow_html=True,
    )
    all_themes = get_all_themes()
    question = st.text_input("Question")
    reponse = st.text_input("reponse")
    theme_flashcard = st.selectbox(
        "Sélectionnez un thème à supprimer", get_all_themes()
    )
    ajouter_flashcard = st.form_submit_button("Ajouter une flashcard")
    if ajouter_flashcard:
        create_card(question, reponse, 1, theme_flashcard[0])
        st.write(f"La flashcard {question} à bien été ajouter.")

st.write("##")
st.write("##")

with st.form("supprimer flashcards"):
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Supprimer flashcards</h1>",
        unsafe_allow_html=True,
    )
    flashcard_a_supprimer = st.selectbox(
        "Sélectionnez une flashcard à supprimer", get_all_cards()
    )
    supprimer_flashcard = st.form_submit_button("Supprimer une flashcard")
    if supprimer_flashcard:
        delete_cards(flashcard_a_supprimer[0])
        st.write(f"La flashcard {flashcard_a_supprimer[1]} à bien été supprimer.")
