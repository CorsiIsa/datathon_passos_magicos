import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data_historico"
DATA_DIR.mkdir(exist_ok=True)

CLASS_PATH = DATA_DIR / "historico_classificacao.xlsx"
REG_PATH = DATA_DIR / "historico_regressao.xlsx"


def render():

    st.title("📊 Histórico de Avaliações")

    # CLASSIFICAÇÃO

    st.subheader("Risco de Desempenho")

    if CLASS_PATH.exists():

        df_class = pd.read_excel(CLASS_PATH)

        st.dataframe(df_class, use_container_width=True)

        with open(CLASS_PATH, "rb") as file:

            st.download_button(
                "Baixar Histórico de Desempenho",
                data=file,
                file_name="historico_classificacao.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        if st.button("Limpar Histórico de Desempenho"):

            CLASS_PATH.unlink()

            st.success("Histórico apagado")
            st.rerun()

    else:
        st.info("Nenhuma classificação registrada.")

    st.divider()

    # REGRESSÃO

    st.subheader("Previsão do INDE")

    if REG_PATH.exists():

        df_reg = pd.read_excel(REG_PATH)

        st.dataframe(df_reg, use_container_width=True)

        with open(REG_PATH, "rb") as file:

            st.download_button(
                "Baixar Histórico do INDE",
                data=file,
                file_name="historico_regressao.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        if st.button("Limpar Histórico do INDE"):

            REG_PATH.unlink()

            st.success("Histórico apagado")
            st.rerun()

    else:
        st.info("Nenhuma previsão registrada.")