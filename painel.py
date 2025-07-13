import streamlit as st
import streamlit_authenticator as stauth
import yfinance as yf
import plotly.graph_objects as go
import toml

# 🔐 Carrega o config.toml
config = toml.load("config.toml")

# ✅ Autenticação corrigida (sem parâmetros nomeados)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Tela de login
name, auth_status, username = authenticator.login("Login", "main")

if auth_status:
    authenticator.logout("Logout", "sidebar")
    st.success(f"Bem-vindo ao Painel Financeiro, {name}! 💹")

    tickers = ["VIVT3.SA", "ITUB4.SA", "VALE3.SA", "PETR4.SA"]

    for ticker in tickers:
        st.subheader(f"📈 {ticker}")
        dados = yf.Ticker(ticker)
        hist = dados.history(period="1mo")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], name=ticker, line=dict(color='deepskyblue')))
        fig.update_layout(template="plotly_dark", margin=dict(l=30, r=30, t=30, b=30))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown("💱 Dólar: R$ 5,54 | Euro: R$ 6,48")
    st.markdown("📰 Fontes: [InfoMoney](https://www.infomoney.com.br/), [Investing](https://br.investing.com/)")

elif auth_status is False:
    st.error("Usuário ou senha incorretos.")
elif auth_status is None:
    st.warning("Por favor, insira suas credenciais.")
