import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import yfinance as yf
import seaborn as sns
import datetime as dt

st.header("My Crypto price webapp")

st.subheader("This app shows the projection of crypto price specify on ")

# plot stock pirce
crypto_list = ['BTC-USD','ETH-USD','BNB-USD','ADA-USD']

df = pd.DataFrame()
today = dt.datetime.now().date().strftime("%Y")
for crypto in crypto_list:
    df[crypto] = yf.Ticker(crypto).history(period='1Y',start="2012-01-01",end="2021-01-01").Close
st.line_chart(df)
#plt.figure()
#plt.plot(df)
#plt.xlabel('Year')
#plt.ylabel('Crypto_price (US Dollar $)')
#plt.legend(['BTC-USD','ETH-USD','BNB-USD','ADA-USD'])
#plt.show()