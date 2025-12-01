import streamlit as st
from projet_flashcards import *
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Vos statistiques", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: black;'>Vos statistiques </h1>",
    unsafe_allow_html=True,
)

st.write("##")
st.divider()
st.write("##")
stats = get_stats()
bonne_reponses = [stat[0] for stat in stats]
mauvaise_reponses = [stat[1] for stat in stats]
date = [stat[2] for stat in stats]
df_stats = pd.DataFrame(
    {
        "Bonne réponse": bonne_reponses,
        "mauvaise réponse": mauvaise_reponses,
        "date": date,
    }
)
if stats:
    fig = px.line(
        df_stats,
        x="date",
        y=["Bonne réponse", "mauvaise réponse"],
        color_discrete_map={"Bonne réponse": "blue", "mauvaise réponse": "red"},
        title="Evolution des réponses correctes et incorrectes par jours",
    )
    fig.update_traces(mode="markers+lines")
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    st.plotly_chart(fig)
else:
    st.write("Il n'y a pas encore de statistiques.")
