import sklearn
import streamlit as st
import pandas as pd

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



