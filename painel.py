import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Painel Financeiro", layout="wide")
st.title("💹 Painel Financeiro Diário")
st.markdown("🔍 Visualização por setor com indicadores financeiros")

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

                # 🎯 Indicadores financeiros
                preco = info.get("currentPrice", "N/A")
                pl = info.get("trailingPE", "N/A")
                dy = info.get("dividendYield", None)
                roe = info.get("returnOnEquity", None)

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("💰 Preço atual", f"R$ {preco}")
                col2.metric("📊 P/L", pl)
                col3.metric("🏦 Dividend Yield", f"{round(dy * 100, 2)}%" if dy else "N/A")
                col4.metric("🧪 ROE", f"{round(roe * 100, 2)}%" if roe else "N/A")

                # 📉 Gráfico de fechamento
                if hist.empty:
                    st.warning(f"⚠️ Sem dados históricos para {ticker}")
                else:
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=hist.index,
                        y=hist['Close'],
                        name=ticker,
                        line=dict(color='deepskyblue')
                    ))
                    fig.update_layout(
                        title=f"{ticker} • Histórico 1 mês",
                        template="plotly_dark",
                        margin=dict(l=40, r=40, t=40, b=40)
                    )
                    st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"Erro ao carregar dados de {ticker}: {e}")
