import streamlit as st
import pandas as pd
import yfinance as yf
import datetime as dt
from sklearn.preprocessing import StandardScaler
st.header("My Crypto price webapp")
st.write("""
Stock **closing price and **volume of crypto of BTC/ETH/BNB/ADA
""")

st.subheader("This line chart shows the projection of crypto price 2021")

# plot stock pirce
crypto_list = ['BTC-USD','ETH-USD','BNB-USD','ADA-USD']

df = pd.DataFrame()
df2 = pd.DataFrame()
today = dt.datetime.now().date().strftime("%Y")
for crypto in crypto_list:
    df[crypto] = yf.Ticker(crypto).history(period='1d',start="2021-01-31",end="2021-12-31").Close
    df2[crypto] = yf.Ticker(crypto).history(period='1d', start="2021-01-31", end="2021-12-31").Volume
#st.line_chart(df)
#st.subheader("This line chart shows the projection of crypto Volume 2021")
#st.line_chart(df2)
st.markdown("##This dataframe shows the closing number of stock price from 2021-01-31 to 2021-12-31")
#st.dataframe(df)
st.table(df)

