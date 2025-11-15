
import streamlit as st
from utils.links import LINKS

st.title("Visão Geral")
st.markdown(
    """
    ### Objetivo
    Descreva aqui o **propósito** do sistema e a **demanda real** atendida.

    ### Público-alvo
    Quem usa? Quais dores resolvemos?

    ### Arquitetura (alto nível)
    - Frontend: **Streamlit**
    - Modelo: **scikit-learn** (ex.: Regressão Logística / Random Forest)
    - Deploy: **Streamlit Community Cloud** (ou Vercel/Render/Azure/GCP/AWS)

    ### Equipe
    Liste aqui **nome (RA) — função** de todos os integrantes.
    """
)

st.divider()
st.subheader("Links")
st.write(f"**Repositório**: {LINKS['repo']}")
st.write(f"**Deploy**: {LINKS['deploy']}")
st.write(f"**Vídeo**: {LINKS['video']}")
