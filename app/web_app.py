import streamlit as st
from app_manager import run_app

st.set_page_config(page_title="GPX Visualizer", layout="centered")
st.title("📍 GPX Visualizer")

title = st.text_input("Podaj tytuł")
uploaded_file = st.file_uploader("Wgraj plik .gpx", type="gpx")


if uploaded_file is not None:
    fig1, buf1, fig2, buf2 = run_app(uploaded_file, title)

    # Wykres hr
    st.pyplot(fig1)
    st.download_button("📥 Pobierz wykres wysokości", buf1, file_name="wysokosc.jpg")

    # Wykres stref slupkowy 
    st.pyplot(fig2)
    st.download_button("📥 Pobierz mapę trasy", buf2, file_name="trasa.jpg")


# streamlit run app/web_app.py