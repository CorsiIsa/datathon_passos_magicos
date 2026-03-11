import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

def render():
    st.header("1. Adequação do nível (IAN)")

    st.markdown(
    "#### Qual é o perfil geral de defasagem dos alunos (IAN) "
        "e como ele evolui ao longo do ano?"
    )

    st.subheader("Distribuição do IAN")
    st.image(str(ASSETS_DIR / "distribuicao_ian.png.jpeg"), caption="Distribuição do IAN")

    st.subheader("Perfil geral de defasagem")
    st.markdown("""
A distribuição do indicador IAN mostra que:
	•	54,2% dos alunos estão no nível 5,0
	•	44,3% estão no nível 10,0
	•	Apenas 1,5% estão no nível 2,5

Isso indica que a base é fortemente concentrada em dois níveis principais (5 e 10), sugerindo que o IAN opera em faixas discretas.

Apenas uma pequena parcela (1,5%) encontra-se no nível mais baixo observado (2,5), indicando que a proporção de alunos com defasagem mais severa é relativamente reduzida.
""")

    st.subheader("Média do IAN por ano")
    st.image(str(ASSETS_DIR / "media_ian_por_ano.jpeg"), caption="Evolução do IAN por ano")

    st.markdown("""
Observa-se uma tendência clara de crescimento do IAN médio ao longo dos anos.

Esse aumento de aproximadamente 1,26 pontos entre 2022 e 2024 sugere melhora no nível de adequação dos alunos nas coortes mais recentes.

Importante destacar que cada ano representa uma coorte distinta de alunos, portanto essa evolução reflete melhora entre turmas, e não necessariamente progresso individual ao longo do tempo.
""")
    
    st.header("2. Desempenho acadêmico (IDA)")

    st.markdown(
    "#### O desempenho acadêmico médio (IDA) está melhorando, "
        "estagnado ou caindo ao longo das fases e anos?"
    )

    st.subheader("Média do IDA por ano")
    st.image(str(ASSETS_DIR / "media_ida_por_ano.jpeg"), caption="Evolução Média do IDA por ano")

    st.markdown("""
Observa-se:

• Crescimento relevante de **2022 para 2023 (+0,57)**  
• Pequena queda em **2024 (-0,31 em relação a 2023)**  
• Mesmo assim, **2024 permanece acima do nível observado em 2022**

Isso indica que o desempenho acadêmico apresentou **melhora inicial seguida de estabilização**, sem evidência de queda estrutural ao longo do período analisado.
""")

    st.subheader("Evolução do IDA por fase")
    st.image(str(ASSETS_DIR / "media_ida_por_fase.jpeg"), caption="IDA médio por fase", use_container_width=True)

    st.subheader("Evolução por fase dentro de cada ano")
    st.markdown("""
O cruzamento ano_referencia x Fase revela um ponto crítico:
- As fases não se repetem entre os anos.
- Cada coorte apresenta fases específicas daquele ciclo.

Isso indica que:

As coortes estão em momentos diferentes do ciclo pedagógico.
Não é correto comparar fases isoladamente entre anos sem considerar progressão.
""")
    
    st.header("3. Engajamento nas atividades (IEG)")

    st.markdown(
    "#### O grau de engajamento dos alunos (IEG) tem relação direta "
        "com seus indicadores de desempenho (IDA) e do ponto de virada (IPV)?"
    )

    st.subheader("Correlação entre os indicadores")
    st.image(
        str(ASSETS_DIR / "correlacao_ieg_ida_ipv.jpeg"),
        caption="Matriz de correlação entre IEG, IDA e IPV"
    )

    st.markdown("""
As correlações observadas entre os principais indicadores foram:

- **IEG x IDA:** 0,54  
- **IEG x IPV:** 0,56  
- **IDA x IPV:** 0,56  

Esses resultados mostram que o **engajamento**, o **desempenho acadêmico** e o **ponto de virada** caminham juntos de forma consistente.

Em especial:

- alunos mais engajados tendem a apresentar **melhor desempenho acadêmico**
- alunos mais engajados também tendem a ter **maior probabilidade de avanço ou recuperação**
- o desempenho acadêmico também está associado ao **ponto de virada**
""")

    st.subheader("Relação entre IEG e desempenho acadêmico (IDA)")
    st.image(
        str(ASSETS_DIR / "ieg_vs_ida.jpeg"),
        caption="Dispersão entre IEG e IDA",
        use_container_width=True
    )

    st.markdown("""
A correlação entre **IEG** e **IDA** é de **0,54**, indicando uma **relação positiva moderada**.

Isso sugere que alunos com maior engajamento nas atividades tendem, em média, a apresentar melhor desempenho acadêmico.

O gráfico de dispersão reforça essa tendência: há maior concentração de alunos com **IDA mais elevado** nas faixas de **IEG entre 7 e 10**.

Embora exista variabilidade individual, o padrão geral indica que **níveis mais altos de engajamento estão associados a melhores resultados acadêmicos**.

De forma geral, os dados indicam que **o engajamento é um fator relevante na trajetória de evolução do aluno**.
""")
    
    st.header("4. Autoavaliação (IAA)")

    st.markdown(
    "#### As percepções dos alunos sobre si mesmos (IAA) são coerentes "
        "com seu desempenho real (IDA) e engajamento (IEG)?"
    )

    st.subheader("Relação estatística")
    st.image(
        str(ASSETS_DIR / "correlacao_iaa_ida_ieg.jpeg"),
        caption="Correlação entre IAA, IDA e IEG"
    )

    st.markdown("""
Correlação observada:

- **IAA ↔ IDA = 0,12**
- **IAA ↔ IEG = 0,13**

Esses valores indicam uma **relação positiva, porém muito fraca** entre a percepção do aluno sobre si mesmo e seu desempenho/engajamento real.

Enquanto isso:

- **IDA ↔ IEG = 0,54**, mostrando que desempenho e engajamento estão de fato alinhados.

Isso sugere que a **autoavaliação do aluno não acompanha de forma consistente seus resultados objetivos**.
""")

    st.subheader("Análise do Gap de Percepção (IAA – IDA)")
    st.markdown("""
Estatísticas do gap:

- **Média:** 1,55
- **Mediana:** 1,80
- **Desvio padrão:** 3,08
- **Mínimo:** -9,0
- **Máximo:** 9,6

A média positiva indica que, em geral, **os alunos tendem a superestimar seu desempenho acadêmico**.
""")

    st.subheader("Distribuição do Gap de Percepção")
    st.image(
        str(ASSETS_DIR / "gap_percepcao_iaa_ida.jpeg"),
        caption="Distribuição do Gap de Percepção (IAA - IDA)",
        use_container_width=True
    )

    st.markdown("""
O histograma mostra:

- concentração maior em **valores positivos**
- **assimetria leve à direita**
- pequeno grupo com **gaps negativos extremos** (subestimação forte)

Isso sugere três perfis comportamentais:

1. **Superestimação predominante** (maioria dos casos)
2. **Percepção relativamente alinhada**
3. **Pequeno grupo que subestima significativamente seu desempenho**
                
Embora os alunos tendam a avaliar-se positivamente, essa percepção apresenta baixa correspondência com seu desempenho e engajamento reais, sugerindo oportunidade de desenvolvimento em autorregulação e consciência de aprendizagem.
""")
    
    st.header("5. Aspectos psicossociais (IPS)")

    st.markdown(
    "#### Há padrões psicossociais (IPS) que antecedem quedas de desempenho "
        "acadêmico ou de engajamento?"
    )

    st.subheader("Desempenho acadêmico por nível de IPS")
    st.image(
        str(ASSETS_DIR / "ida_por_quartil_ips.jpeg"),
        caption="Média do IDA por quartil de IPS"
    )

    st.subheader("Padrão identificado")

    st.markdown("""
Existe uma **tendência clara de aumento do IDA conforme o IPS aumenta**.

Comparando extremos:

- **Quartil inferior IPS → IDA ≈ 6.26**
- **Quartil superior IPS → IDA ≈ 6.81**

Diferença aproximada:

**≈ +0.55 pontos no desempenho acadêmico médio**

O crescimento não é explosivo, mas **consistente**.

Isso sugere que:

- **Melhores condições psicossociais estão associadas a melhor desempenho acadêmico**
- O impacto **não é abrupto**, mas **gradual**
- **Não há evidência de queda de desempenho** nos níveis mais altos de IPS

Assim, o **IPS parece atuar como fator de sustentação do desempenho acadêmico**.

Há **associação positiva entre IPS e desempenho acadêmico**:  
alunos com melhores indicadores psicossociais apresentam, em média, melhor desempenho.

Contudo, com a análise atual:

- **não é possível afirmar causalidade**
- **não é possível garantir precedência temporal**

Ou seja, o IPS pode contribuir para melhores resultados, mas também pode refletir contextos mais favoráveis de aprendizagem.
""")
    
    st.header("6. Aspectos psicopedagógicos (IPP)")

    st.markdown(
    "#### As avaliações psicopedagógicas (IPP) confirmam ou contradizem "
    "a defasagem identificada pelo IAN?"
)

    st.subheader("Relação entre IPP, IDA e IAN")
    st.image(
        str(ASSETS_DIR / "correlacao_ipp_ida_ian.jpeg"),
        caption="Correlação entre IPP, IDA e IAN"
    )

    st.markdown("""
As correlações observadas foram:

- **IPP ↔ IDA = 0,37**
- **IPP ↔ IAN = 0,12**
- **IDA ↔ IAN = 0,12**

Esses resultados mostram que o **IPP tem associação moderada com o desempenho acadêmico atual (IDA)**, mas relação **fraca com a defasagem identificada pelo IAN**.
                
Isso sugere que o **IPP influencia mais o desempenho atual do aluno do que a defasagem estrutural acumulada**.

Portanto, o **IPP não contradiz o IAN**, mas também **não o confirma diretamente**.

Seu efeito parece ocorrer de forma **indireta**, principalmente por meio do impacto no desempenho acadêmico atual.
                
Sendo assim, as avaliações psicopedagógicas apresentam **associação moderada com o desempenho acadêmico (IDA)**, mas **relação fraca com o nível de adequação (IAN)**.

Isso indica que o **IPP influencia mais o desempenho atual do aluno** do que a defasagem estrutural identificada pelo IAN.

Assim, a defasagem parece estar relacionada também a **outros fatores além da dimensão psicopedagógica**, como contexto acumulado, trajetória escolar e condições estruturais de aprendizagem.
""")


    st.header("7.Ponto de Virada do Aluno (IPV)")

    st.markdown("""
    #### Quais comportamentos — acadêmicos, emocionais ou de engajamento — mais influenciam o ponto de virada do aluno (IPV) ao longo do tempo?

    Para responder essa pergunta, foi analisada a correlação entre o IPV e os principais indicadores educacionais.
    """)

    # Tabela de correlação (resultado final)
    corr_data = {
        "Indicador": ["IDA", "IEG", "IAA", "IPS", "IPP", "IAN", "INDE", "IPV"],
        "IDA": [1.00, 0.54, 0.12, 0.02, 0.37, 0.12, 0.79, 0.56],
        "IEG": [0.54, 1.00, 0.13, -0.05, 0.33, -0.06, 0.75, 0.56],
        "IAA": [0.12, 0.13, 1.00, 0.16, 0.05, 0.03, 0.40, 0.06],
        "IPS": [0.02, -0.05, 0.16, 1.00, 0.06, 0.00, 0.20, -0.05],
        "IPP": [0.37, 0.33, 0.05, 0.06, 1.00, 0.12, 0.54, 0.61],
        "IAN": [0.12, -0.06, 0.03, 0.00, 0.12, 1.00, 0.41, 0.15],
        "INDE": [0.79, 0.75, 0.40, 0.20, 0.54, 0.41, 1.00, 0.72],
        "IPV": [0.56, 0.56, 0.06, -0.05, 0.61, 0.15, 0.72, 1.00],
    }

    corr_df = pd.DataFrame(corr_data).set_index("Indicador")

    st.subheader("Tabela de Correlação entre Indicadores")
    st.dataframe(corr_df)

    st.markdown("""
    
    ### O que mais se relaciona ao ponto de virada (IPV)

    O indicador com maior correlação com o IPV é o **INDE (0,72)**.  
    No entanto, o INDE é um indicador global agregado, que sintetiza vários aspectos do desempenho do aluno.  
    Portanto, ele não representa um comportamento específico, mas sim um resultado consolidado.

    Isso indica que o IPV está naturalmente próximo do desempenho geral do aluno.

    ---
                
    ### Entre os comportamentos reais

    Considerando apenas indicadores comportamentais e acadêmicos específicos, os que apresentam maior associação com o IPV são:

    - **IPP (0,61)** → Aspectos psicopedagógicos e técnicos da aprendizagem  
    - **IEG (0,56)** → Participação e engajamento do aluno  
    - **IDA (0,56)** → Desempenho acadêmico direto  

    Esses resultados sugerem que mudanças no desempenho e no engajamento do aluno estão fortemente associadas ao ponto de virada acadêmico.

    ---

    ### O que apresenta pouca influência

    Alguns indicadores apresentam correlação muito baixa com o IPV:

    - **IAA (0,06)** → Autoavaliação do aluno  
    - **IPS (-0,05)** → Aspectos psicossociais  
    - **IAN (0,15)** → Defasagem educacional

    Isso indica que o ponto de virada não está fortemente relacionado à condição estrutural do aluno, mas sim a mudanças recentes no seu comportamento e desempenho.

    ---

    Podemos então concluir que o ponto de virada do aluno (**IPV**) apresenta forte associação com o indicador global de desempenho (**INDE**).  
    Entre os comportamentos específicos, ele se relaciona principalmente com:

    - aspectos psicopedagógicos (**IPP**)
    - nível de engajamento (**IEG**)
    - desempenho acadêmico (**IDA**)

    Por outro lado, fatores estruturais como defasagem educacional (IAN) e autoavaliação (IAA) apresentam baixa associação.

    Esses resultados sugerem que o IPV reflete mais mudanças comportamentais e acadêmicas recentes do que condições estruturais acumuladas ao longo do tempo.
    """)


    st.header("8. Multidimensionalidade dos Indicadores (INDE)")

    st.markdown("""
    ### Quais combinações de indicadores educacionais — desempenho acadêmico, engajamento,aspectos psicossociais e psicopedagógicos — mais influenciam o indicador global do aluno (INDE)?

    Para responder essa pergunta foram analisadas:

    1. Correlação entre os indicadores e o INDE
    2. Modelo de regressão linear para identificar o peso de cada indicador na composição da nota global.
    """)


    # Tabela de correlação com INDE
    corr_data = {
        "Indicador": ["INDE","IDA","IEG","IPV","IPP","IAN","IAA","IPS"],
        "Correlação com INDE": [1.00,0.79,0.75,0.72,0.54,0.41,0.40,0.20]
    }

    corr_df = pd.DataFrame(corr_data)

    st.subheader("Correlação dos Indicadores com o INDE")
    st.dataframe(corr_df, use_container_width=True)


    st.subheader("Resultado do Modelo de Regressão")

    st.caption("Coeficientes da regressão linear utilizando IDA, IEG, IPS e IPP como variáveis explicativas")

    # Tabela de coeficientes do modelo
    modelo_data = {
        "Indicador": ["IEG", "IDA", "IPP", "IPS"],
        "Peso no Modelo": [0.258215, 0.242621, 0.216682, 0.114425]
    }

    modelo_df = pd.DataFrame(modelo_data)

    st.dataframe(modelo_df, use_container_width=True)

    st.metric("R² do Modelo", "0.82")


    st.markdown(""" O modelo de regressão apresentou **R² de aproximadamente 0,82**, indicando que os indicadores analisados
    explicam cerca de 82% da variação do indicador global (INDE).

    Esse resultado sugere que o índice global de desempenho do aluno é fortemente influenciado
    por essas dimensões educacionais.

    ---

    ### Indicadores com maior influência

    Entre os indicadores analisados, os que apresentam maior peso no modelo são:

    - **IEG (0,26)** → Engajamento e participação do aluno  
    - **IDA (0,24)** → Desempenho acadêmico direto  
    - **IPP (0,22)** → Aspectos psicopedagógicos  

    Esses fatores representam dimensões diretamente ligadas ao comportamento e ao desempenho educacional.

    ---

    ### Indicadores com menor influência

    O indicador **IPS (0,11)** apresenta influência menor no modelo,
    indicando que fatores psicossociais isoladamente possuem menor impacto direto
    sobre o indicador global de desempenho.

    ---
    Com esses resultados entendemos que a combinação de desempenho acadêmico (IDA), engajamento (IEG),
    aspectos psicopedagógicos (IPP) e psicossociais (IPS)explica aproximadamente
    82% da variação do indicador global (INDE).

    Entre esses fatores, **o engajamento apresenta o maior peso no modelo**,
    seguido pelo desempenho acadêmico e pela dimensão psicopedagógica.

    Esses resultados indicam que o INDE é mais sensível a variáveis comportamentais
    e acadêmicas do que a fatores psicossociais isolados, reforçando a importância
    do engajamento do aluno no processo educacional.
    """)

    st.header("9.Previsão de Risco")

    st.markdown("""
    ### Quais padrões nos indicadores permitem identificar alunos em risco antes de uma queda no desempenho acadêmico?

    Para responder essa pergunta foi construído um modelo de Machine Learning utilizando Regressão Logística, com o objetivo de estimar a probabilidade de um aluno entrar em situação de risco.

    O risco foi definido como baixo desempenho acadêmico (IDA < 5).
    """)

    st.caption("Variáveis utilizadas no modelo preditivo:")

    features_df = pd.DataFrame({
        "Indicadores Utilizados": ["IEG", "IPP", "IPS", "IAA", "IAN"]
    })

    st.dataframe(features_df, use_container_width=True)


    st.subheader("Desempenho do Modelo")

    metricas_df = pd.DataFrame({
        "Métrica": ["Accuracy", "AUC", "Precision (classe risco)", "Recall (classe risco)", "F1-score (classe risco)"],
        "Valor": ["0.80", "0.76", "0.40", "0.23", "0.29"]
    })

    st.dataframe(metricas_df, use_container_width=True)


    st.subheader("Importância dos Indicadores no Modelo")

    coef_df = pd.DataFrame({
        "Indicador": ["IPS", "IAN", "IAA", "IPP", "IEG"],
        "Coeficiente do Modelo": [0.033, -0.012, -0.034, -0.469, -0.681]
    })

    st.dataframe(coef_df, use_container_width=True)


    st.markdown("""
                
    ### Capacidade preditiva do modelo

    Após eliminar possíveis fontes de vazamento de informação, foi treinado um modelo de Regressão Logística para prever o risco de queda no desempenho acadêmico.

    O modelo apresentou **AUC de aproximadamente 0,76**, indicando capacidade moderada de discriminação entre alunos em risco e alunos fora de risco.

    A acurácia geral foi de aproximadamente **80%**, embora o desempenho para identificar especificamente alunos em risco ainda seja limitado, refletido em valores menores de recall e F1-score para essa classe.

    ---

    ### Indicadores com maior impacto

    Entre as variáveis analisadas, os coeficientes do modelo indicam que:

    - **IEG (engajamento)** apresenta o maior efeito protetivo
    - **IPP (aspectos psicopedagógicos)** também contribui para reduzir o risco

    Isso sugere que níveis mais altos de engajamento e melhor desenvolvimento pedagógico estão associados a menor probabilidade de queda de desempenho.

    ---

    ### Indicadores com menor influência

    Os indicadores abaixo apresentaram baixo impacto no modelo:

    - **IAA (autoavaliação do aluno)**
    - **IPS (aspectos psicossociais)**
    - **IAN (adequação estrutural)**

    Esses fatores parecem ter menor capacidade de prever diretamente o risco de queda de desempenho acadêmico.

    ---
    Os resultados indicam que variáveis comportamentais e pedagógicas antecedem a queda de desempenho acadêmico.

    O modelo sugere que engajamento do aluno (IEG) e aspectos psicopedagógicos (IPP) são os principais fatores associados à redução do risco.

    Isso indica que intervenções focadas no aumento do engajamento podem atuar como mecanismo preventivo relevante, permitindo identificar alunos em risco antes que a queda de desempenho se consolide.
    """)

    st.header("10.Efetividade do Programa")

    st.markdown("""
    ### Os indicadores educacionais mostram melhora consistente ao longo do ciclo nas diferentes fases (Quartzo, Ágata, Ametista e Topázio), indicando impacto real do programa educacional?

    A classificação dos alunos é baseada no indicador global INDE, conforme os intervalos:

    - **Quartzo** → 2.405 a 5.506  
    - **Ágata** → 5.506 a 6.868  
    - **Ametista** → 6.868 a 8.230  
    - **Topázio** → 8.230 a 9.294
    """)

    # Evolução média dos indicadores por ano

    st.subheader("Evolução Média dos Indicadores por Ano")

    df_ano = pd.DataFrame({
        "Ano": [2022, 2023, 2024],
        "IDA": [6.09, 6.66, 6.35],
        "IEG": [7.89, 8.70, 7.37],
        "IAN": [6.42, 7.24, 7.68],
        "IPV": [7.25, 8.03, 7.35],
        "IPP": [None, 7.56, 7.55],
        "IPS": [6.90, 5.12, 6.83],
        "INDE": [7.04, 7.34, 7.40]
    })

    st.dataframe(df_ano, use_container_width=True)


    # Distribuição das categorias por ano

    st.subheader("Distribuição das Classificações (Pedras) por Ano")

    pedras_df = pd.DataFrame({
        "Ano": [2022, 2023, 2024],
        "Quartzo": [0.082, 0.024, 0.054],
        "Ágata": [0.302, 0.281, 0.229],
        "Ametista": [0.530, 0.525, 0.501],
        "Topázio": [0.086, 0.170, 0.215]
    })

    st.dataframe(pedras_df, use_container_width=True)


    st.markdown("""
    ### Evolução do indicador global

    A média do **INDE** apresentou crescimento ao longo do período analisado:

    - 2022 → **7.04**
    - 2023 → **7.34**
    - 2024 → **7.40**

    Esse comportamento sugere melhora consistente no desempenho global dos alunos ao longo do ciclo do programa.

    ---

    ### Redução da defasagem educacional

    O indicador IAN (adequação educacional) apresentou crescimento contínuo:

    - 6.42 → 7.24 → 7.68

    Esse aumento indica redução estrutural da defasagem ao longo dos anos, sugerindo melhora na adequação educacional dos alunos.

    ---

    ### Mudança na distribuição das classificações

    A análise das classificações baseadas no INDE reforça esse padrão de evolução:

    **Topázio (nível mais alto)**  
    - 8.6% → 17.0% → 21.5%

    A proporção de alunos nesse nível mais que dobrou entre 2022 e 2024.

    ---

    **Quartzo (nível mais baixo)**  
    - 8.2% → 2.4% → 5.4%

    Observa-se forte redução em 2023, com leve aumento em 2024, mas ainda abaixo do nível inicial.

    ---

    **Ametista (nível intermediário alto)**  

    Houve pequena redução percentual (53% → 50%), indicando possível migração de parte desses alunos para níveis superiores.

    ---

    ### Oscilações em indicadores comportamentais

    Indicadores como engajamento (IEG) e desempenho acadêmico (IDA) apresentaram oscilações entre os anos,
    com pico em 2023 e leve retração em 2024.

    Isso sugere que nem todas as dimensões evoluem de forma uniforme ao longo do tempo.

    ---

    A análise da evolução dos indicadores entre 2022 e 2024 mostra evidências relevantes de melhora estrutural ao longo do ciclo do programa.

    O crescimento do **INDE**, aliado à melhora contínua no **IAN**, indica evolução global consistente no desempenho e na adequação educacional dos alunos.

    A mudança na distribuição das classificações também reforça esse padrão, com aumento expressivo na proporção de alunos no nível **Topázio** e redução relativa do nível **Quartzo**.

    Entretanto, por se tratar de análise observacional sem grupo de controle, os resultados indicam associação temporal com evolução dos indicadores, mas não permitem afirmar causalidade isolada do programa.
    """)