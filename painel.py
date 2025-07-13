import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Painel Financeiro", layout="wide")
st.title("💹 Painel Financeiro Diário")
st.markdown("🔓 Modo teste — painel sem autenticação")

# Lista de ações
tickers = ["VIVT3.SA", "ITUB4.SA", "VALE3.SA", "PETR4.SA"]

# Gráficos interativos
for ticker in tickers:
    st.subheader(f"📈 {ticker}")
    try:
        dados = yf.Ticker(ticker)
        hist = dados.history(period="1mo")

        if hist.empty:
            st.warning(f"⚠️ Sem dados disponíveis para {ticker}")
        else:
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=hist.index, y=hist['Close'],
                name=ticker, line=dict(color='deepskyblue')
            ))
            fig.update_layout(
                title=f"{ticker}",
                template="plotly_dark",
                margin=dict(l=30, r=30, t=30, b=30)
            )
            st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Erro ao carregar {ticker}: {e}")

# Informações complementares
st.markdown("---")
st.markdown("💱 Câmbio hoje: Dólar R$ 5,54 | Euro R$ 6,48")
st.markdown("📰 Fontes: [InfoMoney](https://www.infomoney.com.br/) | [Investing](https://br.investing.com/)")
