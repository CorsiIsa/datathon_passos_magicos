import streamlit as st
from pathlib import Path

def render():

    BASE_DIR = Path(__file__).resolve().parent
    IMAGE_PATH = BASE_DIR / "assets" / "1.png"

    st.image(IMAGE_PATH, use_container_width=True)

    st.title("Análise de Dados e Suporte à Decisão")

    st.markdown("""
    Este aplicativo foi desenvolvido para apoiar a análise dos dados do programa da Associação Passos Mágicos, utilizando técnicas de Machine Learning para auxiliar no acompanhamento do desenvolvimento dos alunos e apoiar a tomada de decisões.

    Por meio da plataforma, é possível analisar indicadores relacionados ao desenvolvimento dos estudantes, incluindo aspectos acadêmicos, emocionais e de engajamento, permitindo uma visão mais completa da trajetória de cada aluno no programa.

    Se for sua primeira vez utilizando o sistema, recomendamos começar pelos indicadores apresentados abaixo, que explicam as principais métricas utilizadas nas análises e predições.
    """)

    st.markdown("## Indicadores do Programa")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("**IAN — Indicador Acadêmico de Nível** \n\nMostra se o aluno está no nível esperado para sua série ou se existe defasagem no aprendizado.")
        
        st.info("**IEG — Indicador de Engajamento** \n\nIndica o nível de participação e envolvimento do aluno nas atividades.")

        st.info("**IPS — Indicador Psicossocial** \n\nAvalia fatores emocionais e sociais que podem influenciar o aprendizado.")

    with col2:
        st.info("**IDA — Indicador de Desempenho Acadêmico** \n\nRepresenta o desempenho geral do aluno nas atividades educacionais.")

        st.info("**IAA — Indicador de Autoavaliação** \n\nReflete como o próprio aluno percebe seu desempenho e evolução.")

        st.info("**IPP — Indicador Psicopedagógico** \n\nAvaliação técnica voltada para identificar dificuldades de aprendizagem.")

    with col3:
        st.info("**IPV — Indicador de Evolução** \n\nAponta momentos de mudança ou evolução significativa na trajetória do aluno.")

        st.success("**INDE — Indicador de Desenvolvimento Educacional** \n\nIndicador consolidado que representa o desempenho geral do aluno.")

