import streamlit as st
import joblib
from pathlib import Path

# Caminho base do projeto

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

CLASSIFICATION_PATH = MODEL_DIR / "classification_model.pkl"
REGRESSION_PATH = MODEL_DIR / "regression_model.pkl"


# Inicialização do session_state

def init_state():
    if "classification_model" not in st.session_state:
        st.session_state.classification_model = joblib.load(CLASSIFICATION_PATH)

    if "regression_model" not in st.session_state:
        st.session_state.regression_model = joblib.load(REGRESSION_PATH)
