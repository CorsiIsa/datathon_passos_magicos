import streamlit as st
import pandas as pd

def render():

    st.title("Projeção do Desempenho Educacional (INDE)")

    model = st.session_state.regression_model

    st.write("Insira os valores dos indicadores:")

    # Pegando os valores já no formato necessário
    IDA = st.number_input("IDA", min_value=0.0, format="%.2f")
    IEG = st.number_input("IEG", min_value=0.0, format="%.2f")
    IPS = st.number_input("IPS", min_value=0.0, format="%.2f")
    IPP = st.number_input("IPP", min_value=0.0, format="%.2f")

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