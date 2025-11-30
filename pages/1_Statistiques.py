import streamlit as st
from projet_flashcards import *
import plotly.express as px

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
st.write(f"{bonne_reponses}")
st.write(f"{mauvaise_reponses}")
if len(stats) != 0:
    fig = px.line(
        x=date,
        y=[bonne_reponses, mauvaise_reponses],
        color_discrete_map={"bonnes_reponses": "blue", "mauvaises_reponses": "red"},
        title="Evolution des réponses correctes et incorrectes par jours",
    )
    fig.update_traces(mode="markers+lines")
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    st.plotly_chart(fig)
    st.write("##")
    st.divider()
    st.write("##")
    today = datetime.now().strftime("%Y-%m-%d")
    today_stat = [[stat[0], stat[1]] for stat in stats if stat[-1] == today]
    fig = px.pie(values=today_stat, names=today_stat, color=today_stat, hole=0.3)
    st.plotly_chart(fig)
else:
    st.write("Il n'y a pas encore de statistiques.")
