import streamlit as st
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