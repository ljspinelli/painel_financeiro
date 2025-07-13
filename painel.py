import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Painel Financeiro", layout="wide")
st.title("💹 Painel Financeiro Diário")
st.markdown("🔍 Visualização por setor com indicadores")

# 🔢 Separação por setor
setores = {
    "🏦 Bancos": ["ITUB4.SA", "BBDC4.SA"],
    "⚙️ Indústria / Commodities": ["VALE3.SA", "PETR4.SA"],
    "📞 Telecom": ["VIVT3.SA"]
}

# 📑 Abas por setor
abas = st.tabs(list(setores.keys()))

# 📈 Renderizar cada aba
for nome_setor, aba in zip(setores.keys(), abas):
    with aba:
        for ticker in setores[nome_setor]:
            st.subheader(f"📊 {ticker}")

            try:
                dados = yf.Ticker(ticker)
                info = dados.info
                hist = dados.history(period="1mo")

                # 🎯 Indicadores extraídos
                preco = info.get("currentPrice", "N/A")
                pl = info.get("trailingPE", "N/A
