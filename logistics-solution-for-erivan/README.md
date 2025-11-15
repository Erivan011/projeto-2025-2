
# Logistics Solution — Sistema WEB

**Objetivo**: disponibilizar como **aplicação WEB** o projeto de Ciência de Dados/Logística, atendendo aos requisitos da disciplina (deploy em Cloud, versionamento no GitHub, vídeo no YouTube e identificação do grupo).

## 🚀 Links
- **Deploy (produção)**: _adicione aqui o URL após publicar (ex.: Streamlit Cloud)_
- **Vídeo (YouTube)**: _adicione aqui o link do vídeo (≥ 5 minutos, público ou não listado)_

## 👥 Integrantes do Grupo
- Nome (RA) — função
- Nome (RA) — função
- _adicione todos os integrantes (6 a 12)_

## 🧩 Tecnologias
- Python, Streamlit, pandas, scikit-learn, matplotlib, seaborn

## 📦 Estrutura
```text
.
├── app.py                 # aplicação Streamlit
├── requirements.txt       # dependências
├── README.md              # este arquivo
└── .streamlit/
    └── config.toml        # tema (opcional)
```

## 🛠️ Como rodar localmente
```bash
# 1) Clonar o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPO.git
cd SEU_REPO

# 2) (Opcional) criar venv
python -m venv .venv && source .venv/bin/activate  # Linux/macOS
# ou
# py -m venv .venv && .venv\Scriptsctivate      # Windows

# 3) Instalar dependências
pip install -r requirements.txt

# 4) Executar
streamlit run app.py
```

## ☁️ Como publicar no Streamlit Community Cloud
1. Faça _push_ deste repositório no GitHub.  
2. Acesse [https://share.streamlit.io](https://share.streamlit.io) e conecte sua conta do GitHub.  
3. Clique em **New app** → selecione este repositório → branch `main` → **file**: `app.py`.  
4. Publique. Copie o **URL público** e adicione no topo deste README.

## 📝 Requisitos da disciplina — checklist
- [ ] Sistema WEB online (link acima)  
- [x] Versionamento no GitHub  
- [ ] Integrantes listados neste README  
- [ ] Vídeo (YouTube) adicionado  
- [ ] Formulário de entrega preenchido quando disponível  

## 📄 Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE`.
