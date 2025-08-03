import streamlit as st
import re
from datetime import datetime
from app_manager import run_app

def prepare_title(title):
    if title is None or title == "":
        return datetime.now().strftime("%Y.%m.%d") + " Trening"
    else:
        # Dozwolone znaki dla nazwy pliku: litery, cyfry, spacja, myślnik, podkreślnik
        safe_title = re.sub(r'[<>:"/\\|?*\n\r\t]', '', title)
        return safe_title
        

def main():
    st.set_page_config(page_title="GPX Visualizer", layout="centered")
    st.title("📍 GPX Visualizer")

    file_title = prepare_title(st.text_input("Podaj tytuł"))
    uploaded_file = st.file_uploader("Wgraj plik .gpx", type="gpx")

    if uploaded_file is not None:
        fig1, buf1, fig2, buf2 = run_app(uploaded_file, file_title)

        # Wykres hr
        st.pyplot(fig1)
        st.download_button("📥 Pobierz wykres liniowy HR", buf1, file_name='HR ' + file_title + '.jpg')

        # Wykres stref slupkowy 
        st.pyplot(fig2)
        st.download_button("📥 Pobierz wykres słupkowy stref HR", buf2, file_name=file_title + '.jpg')

if __name__ == "__main__":
    main()


# streamlit run app/web_app.py