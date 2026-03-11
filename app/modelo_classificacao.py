import sklearn
import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

def render():
    
    st.title("Análise de Risco de Defasagem Acadêmica")

    model = st.session_state.classification_model

    st.write("Insira os valores dos indicadores:")

    #Estamos pegando os valores com os formatos necessários
    IEG = st.number_input("IEG", min_value=0.0, format="%.2f")
    IPP = st.number_input("IPP", min_value=0.0, format="%.2f")
    IPS = st.number_input("IPS", min_value=0.0, format="%.2f")
    IAA = st.number_input("IAA", min_value=0.0, format="%.2f")
    IAN = st.number_input("IAN", min_value=0.0, format="%.2f")

    # Caminho do arquivo para salvar o histórico
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data_historico"
    DATA_DIR.mkdir(exist_ok=True)

    DATA_PATH = DATA_DIR / "historico_classificacao.xlsx"

    #Para usar o nosso modelo, precisamos criar um df com os nomes das variáveis que usamos no treinamento
    if st.button("Classificar"):

        #Criando o DF que iremos passar para o modelo
        input_data = pd.DataFrame({
            "IEG": [IEG],
            "IPP": [IPP],
            "IPS": [IPS],
            "IAA": [IAA],
            "IAN": [IAN]
        })

        #Pegando o resultado
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        #Exibindo o resultado no front
        if prediction == 1:
            st.error("O aluno apresenta um risco")
        else:
            st.success("O aluno não apresenta nenhum risco")

        st.info(f"Probabilidade de risco: {probability:.2%}")

        # registro
        registro = {
            "Data": datetime.now(),
            "IEG": IEG,
            "IPP": IPP,
            "IPS": IPS,
            "IAA": IAA,
            "IAN": IAN,
            "Probabilidade_Risco": probability,
            "Classificação": "Risco" if prediction == 1 else "Sem Risco"
        }

        df_novo = pd.DataFrame([registro])

        # salvar no Excel
        if DATA_PATH.exists():

            df_antigo = pd.read_excel(DATA_PATH)
            df_final = pd.concat([df_antigo, df_novo], ignore_index=True)

        else:

            df_final = df_novo

        df_final.to_excel(DATA_PATH, index=False)

        st.success("Registro salvo no histórico!")

  