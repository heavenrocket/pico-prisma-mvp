import streamlit as st
import pandas as pd
from utils.nlp_extractor import extract_pico

st.title("🧠 Extractor automático PICO + Diagrama PRISMA")

uploaded_file = st.file_uploader("Carga tu archivo de abstracts (.csv)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    pico_data = []
    for _, row in df.iterrows():
        pico = extract_pico(row["Abstract"])
        pico["Autor"] = row["Autores"]
        pico_data.append(pico)

    result_df = pd.DataFrame(pico_data)
    st.write("📋 Tabla PICO Generada")
    st.dataframe(result_df)

    st.download_button("Descargar tabla PICO", result_df.to_csv(index=False), file_name="tabla_pico.csv")
