import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score


def load_and_prepare_data():
    arquivo = r"data\BASE DE DADOS PEDE 2024 - DATATHON (1).xlsx"

    df_2022 = pd.read_excel(arquivo, sheet_name="PEDE2022")
    df_2023 = pd.read_excel(arquivo, sheet_name="PEDE2023")
    df_2024 = pd.read_excel(arquivo, sheet_name="PEDE2024")

    df_2022["ano_referencia"] = 2022
    df_2023["ano_referencia"] = 2023
    df_2024["ano_referencia"] = 2024

    df_2022 = df_2022.rename(columns={
        "Ano nasc": "ano_nascimento",
        "Nome": "nome",
        "Gênero": "genero",
        "Ano ingresso": "ano_ingresso",
        "Instituição de ensino": "instituicao_ensino",
        "INDE 22": "INDE"
    })

    df_2023 = df_2023.rename(columns={
        "Nome Anonimizado": "nome",
        "Data de Nasc": "data_nascimento",
        "Gênero": "genero",
        "Ano ingresso": "ano_ingresso",
        "Instituição de ensino": "instituicao_ensino",
        "INDE 2023": "INDE"
    })

    df_2024 = df_2024.rename(columns={
        "Nome Anonimizado": "nome",
        "Data de Nasc": "data_nascimento",
        "Gênero": "genero",
        "Ano ingresso": "ano_ingresso",
        "Instituição de ensino": "instituicao_ensino",
        "INDE 2024": "INDE"
    })

    # Datas
    df_2022["ano_nascimento"] = pd.to_numeric(df_2022["ano_nascimento"], errors="coerce")

    df_2023["data_nascimento"] = pd.to_datetime(df_2023["data_nascimento"], errors="coerce")
    df_2023["ano_nascimento"] = df_2023["data_nascimento"].dt.year

    df_2024["data_nascimento"] = pd.to_datetime(df_2024["data_nascimento"], errors="coerce")
    df_2024["ano_nascimento"] = df_2024["data_nascimento"].dt.year

    for df in [df_2022, df_2023, df_2024]:
        df["idade"] = df["ano_referencia"] - df["ano_nascimento"]

    # Converter indicadores
    indicadores = ["INDE", "IAA", "IEG", "IPS", "IDA", "IPV", "IAN", "IPP"]

    for df in [df_2022, df_2023, df_2024]:
        for col in indicadores:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

    colunas_padrao = [
        "RA", "nome", "ano_referencia", "ano_nascimento", "idade",
        "genero", "ano_ingresso", "instituicao_ensino",
        "Fase", "Turma",
        "INDE", "IAA", "IEG", "IPS", "IDA", "IPV", "IAN", "IPP"
    ]

    df_2022_clean = df_2022[[c for c in colunas_padrao if c in df_2022.columns]]
    df_2023_clean = df_2023[[c for c in colunas_padrao if c in df_2023.columns]]
    df_2024_clean = df_2024[[c for c in colunas_padrao if c in df_2024.columns]]

    df_final = pd.concat(
        [df_2022_clean, df_2023_clean, df_2024_clean],
        ignore_index=True
    )

    return df_final


def train_classification_model():
    df_final = load_and_prepare_data()

    df_final["risco"] =  (df_final["IDA"] < 5).astype(int)

    features = ["IEG", "IPP", "IPS", "IAA", "IAN"]

    df_model = df_final[features + ["risco"]].dropna()

    X = df_model[features]
    y = df_model["risco"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]

    report = classification_report(y_test, pred, output_dict=False)
    auc = roc_auc_score(y_test, proba)
    coeficientes = pd.Series(model.coef_[0], index=features).sort_values(ascending=False)

    print(report)
    print(auc)
    print(coeficientes)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/classification_model.pkl")

    print("Modelo de classificação salvo com sucesso!")


if __name__ == "__main__":
    train_classification_model()