
import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, RocCurveDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Logistics Solution • Demo", layout="wide")

st.title("Logistics Solution — Sistema WEB (Demo)")
st.write(
    """
    Este app é um **template** para publicar seu projeto de Ciência de Dados/Logística como **Sistema WEB**.
    Faça o **upload** de um CSV, defina a coluna alvo e selecione um modelo para treinar e avaliar.

    > Substitua/expanda este template com as regras de negócio e análises do seu notebook.
    """
)

with st.sidebar:
    st.header("Configurações")
    st.markdown("**1) Dados**")
    uploaded = st.file_uploader("Envie um arquivo CSV (UTF-8)", type=["csv"]) 
    st.markdown("**2) Pré-processamento**")
    scale_features = st.checkbox("Padronizar variáveis numéricas (StandardScaler)", value=True)
    test_size = st.slider("Tamanho do conjunto de teste", 0.1, 0.4, 0.2, 0.05)
    random_state = st.number_input("Random state", min_value=0, value=42, step=1)
    st.markdown("**3) Modelo**")
    model_name = st.selectbox("Escolha o modelo", ["Logistic Regression", "Random Forest (Classificação)"])

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

def build_model(name):
    if name == "Logistic Regression":
        clf = LogisticRegression(max_iter=500)
    else:
        clf = RandomForestClassifier(n_estimators=300, random_state=random_state)
    return clf

if uploaded is not None:
    df = load_data(uploaded)
    st.subheader("Prévia dos dados")
    st.dataframe(df.head())

    # Seleção de alvo e features
    st.subheader("Configurar experimento")
    target = st.selectbox("Selecione a coluna alvo (classificação)", options=df.columns)
    feature_cols = st.multiselect(
        "Selecione as features (se vazio, usaremos todas as colunas exceto a alvo)",
        options=[c for c in df.columns if c != target]
    )
    if not feature_cols:
        feature_cols = [c for c in df.columns if c != target]

    # Separar X, y
    X = df[feature_cols].copy()
    y = df[target].copy()

    # Converter categóricas automaticamente (one-hot)
    X = pd.get_dummies(X, drop_first=True)

    # Treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y if y.nunique() < 20 else None
    )

    # Escalonamento
    if scale_features:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # Treinar
    clf = build_model(model_name)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)

    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Accuracy", f"{accuracy_score(y_test, preds):.3f}")
    col2.metric("Precision", f"{precision_score(y_test, preds, average='weighted', zero_division=0):.3f}")
    col3.metric("Recall", f"{recall_score(y_test, preds, average='weighted', zero_division=0):.3f}")
    col4.metric("F1-score", f"{f1_score(y_test, preds, average='weighted', zero_division=0):.3f}")

    # Matriz de confusão
    st.subheader("Matriz de Confusão")
    fig, ax = plt.subplots(figsize=(6,4))
    cm = confusion_matrix(y_test, preds)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_xlabel('Predito')
    ax.set_ylabel('Real')
    st.pyplot(fig)

    # ROC-AUC (binária)
    if y.nunique() == 2:
        st.subheader("Curva ROC")
        try:
            if hasattr(clf, "predict_proba"):
                y_prob = clf.predict_proba(X_test)[:,1]
            else:
                y_prob = clf.decision_function(X_test)
            auc = roc_auc_score(y_test, y_prob)
            st.write(f"ROC-AUC: **{auc:.3f}**")
            RocCurveDisplay.from_predictions(y_test, y_prob)
            st.pyplot(plt.gcf())
        except Exception as e:
            st.info(f"Não foi possível traçar a ROC: {e}")

    # Download de previsões
    st.subheader("Exportar previsões")
    out = pd.DataFrame({"y_true": y_test, "y_pred": preds})
    st.download_button("Baixar CSV de previsões", out.to_csv(index=False).encode('utf-8'), file_name="predicoes.csv", mime="text/csv")

else:
    st.info(
        "Envie um CSV na barra lateral para iniciar. Dica: exporte os dados limpos do seu notebook e faça o upload aqui."
    )

st.markdown("""
---
**Sobre este projeto**  
Repositório GitHub: [SUBSTITUA_PELO_LINK_DO_REPO](https://github.com/SEU_USUARIO/SEU_REPO)  
Deploy: [SUBSTITUA_PELO_LINK_DO_DEPLOY](https://example.streamlit.app)  
Vídeo (YouTube): [link aqui]
""")
