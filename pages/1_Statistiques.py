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

if stats:
    fig = px.line(
        x=stats[3],
        y=[stats[1], stats[2]],
        color_discrete_map={"bonnes_reponses": "blue", "mauvaises_reponses": "red"},
        title="Evolution des réponses correctes et incorrectes par jours",
    )
    fig.update_traces(mode="markers+lines")
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    fig.show()
    st.write("##")
    st.divider()
    st.write("##")
    today = datetime.now().strftime("%Y-%m-%d")
    today_stat = [[stat[1], stat[2]] for stat in stats if stat[-1] == today]
    fig = px.pie(values=today_stat, names=today_stat, color=today_stat, hole=0.3)
    fig.show()
else:
    st.write("Il n'y a pas encore de statistiques.")
