import streamlit as st
import menu,modelo_classificacao,modelo_regressao,analise,historico
from analise import render as render_analise

from state import init_state

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ICON_PATH = BASE_DIR / "assets" / "2.png"

init_state()

st.set_page_config(
    page_title="Passos Mágicos",
    page_icon=str(ICON_PATH),
)

if "pagina" not in st.session_state:
    st.session_state.pagina = "Menu"

with st.sidebar:
    st.markdown("## Navegação")

    if st.button("Menu"):
        st.session_state.pagina = "Menu"

    if st.button("Modelo Classificação"):
        st.session_state.pagina = "Modelo Classificação"

    if st.button("Modelo Regressão"):
        st.session_state.pagina = "Modelo Regressão"

    if st.button("Histórico"):
        st.session_state.pagina = "Histórico"

    if st.button("Análise"):
        st.session_state.pagina = "Análise"

if st.session_state.pagina == "Menu":
    menu.render()
elif st.session_state.pagina == "Modelo Classificação":
    modelo_classificacao.render()
elif st.session_state.pagina == "Modelo Regressão":
    modelo_regressao.render()
elif st.session_state.pagina == "Análise":
    analise.render()
elif st.session_state.pagina == "Histórico":
    historico.render()