import streamlit as st
import streamlit_authenticator as stauth
import yfinance as yf
import plotly.graph_objects as go
import toml

config = toml.load("config.toml")
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, auth_status, username = authenticator.login("Login", "main")

if auth_status:
    st.success(f"Bem-vindo, {name}!")
    authenticator.logout("Logout", "sidebar")

    st.title("💹 Painel Financeiro Diário")
    tickers = ["VIVT3.SA", "ITUB4.SA", "VALE3.SA", "PETR4.SA"]
    
    for t in tickers:
        st.subheader(t)
        dados = yf.Ticker(t)
        hist = dados.history(period="1mo")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], name=t))
        fig.update_layout(title=f"{t}", xaxis_title="Data", yaxis_title="Preço", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

elif auth_status is False:
    st.error("Usuário ou senha incorretos.")
elif auth_status is None:
    st.warning("Digite suas credenciais para acessar o painel.")
