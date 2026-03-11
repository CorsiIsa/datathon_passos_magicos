import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

def render():

    st.title("Projeção do Desempenho Educacional (INDE)")

    model = st.session_state.regression_model

    st.write("Insira os valores dos indicadores:")

    # Pegando os valores já no formato necessário
    IDA = st.number_input("IDA", min_value=0.0, format="%.2f")
    IEG = st.number_input("IEG", min_value=0.0, format="%.2f")
    IPS = st.number_input("IPS", min_value=0.0, format="%.2f")
    IPP = st.number_input("IPP", min_value=0.0, format="%.2f")


    # Caminho do arquivo para salvar o histórico
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data_historico"
    DATA_DIR.mkdir(exist_ok=True)

    DATA_PATH = DATA_DIR / "historico_regressao.xlsx"

    #Para usar o nosso modelo, precisamos criar um df com os nomes das variáveis que usamos no treinamento
    if st.button("Prever"):
        
        #Criando o DF que iremos passar para o modelo
        input_data = pd.DataFrame({
            "IDA": [IDA],
            "IEG": [IEG],
            "IPS": [IPS],
            "IPP": [IPP]
        })

        #Pegando a resposta do modelo
        prediction = model.predict(input_data)

        #Exibindo a resposta 
        st.success(f"INDE previsto: {prediction[0]:.2f}")

        # Registro
        registro = {
            "Data": datetime.now(),
            "IDA": IDA,
            "IEG": IEG,
            "IPS": IPS,
            "IPP": IPP,
            "INDE_previsto": prediction
        }

        df_novo = pd.DataFrame([registro])

        # Salvar no Excel
        if DATA_PATH.exists():

            df_antigo = pd.read_excel(DATA_PATH)
            df_final = pd.concat([df_antigo, df_novo], ignore_index=True)

        else:

            df_final = df_novo

        df_final.to_excel(DATA_PATH, index=False)

        st.success("Registro salvo no histórico!")