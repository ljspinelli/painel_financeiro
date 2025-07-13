import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Painel Financeiro", layout="wide")

st.title("💹 Painel Financeiro Diário")
st.markdown("Visualização de ações sem login — modo teste 🧪")

# Lista de ativos para exibição
tickers = ["VIVT3.SA", "ITUB4.SA", "VALE3.SA", "PETR4.SA"]

# Gerar gráficos
for ticker in tickers:
    st.subheader(f"📈 {ticker}")
    dados = yf.Ticker(ticker)
    hist = dados.history(period="1mo")

    # Verificação de dados antes de traçar
    if hist.empty:
        st.warning(f"⚠️ Não foi possível carregar dados para {ticker}.")
    else:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], name=ticker, line=dict(color='deepskyblue')))
        fig.update_layout(template="plotly_dark", margin=dict(l=30, r=30, t=30, b=30))
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("💱 Dólar: R$ 5,54 | Euro: R$ 6,48")
st.markdown("📰 Fontes: [InfoMoney](https://www.infomoney.com.br/) | [Investing](https://br.investing.com/)")
