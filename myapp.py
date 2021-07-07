import streamlit as st
import pandas as pd
import yfinance as yf
import datetime as dt
from sklearn.preprocessing import StandardScaler

st.header("My Crypto price webapp")
st.write("""
Stock **closing price and **volume of crypto of BTC/ETH/BNB/ADA
""")

st.image("crypto.jpg",width=650)

st.subheader("This line chart shows the projection of crypto price 2021")

# plot stock pirce
crypto_list = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD']
input_crypto = st.radio("Please select your Coin",["BTC-USD","ETH-USD","BNB-USD","ADA-USD","See-Comparison"],index=1)
df = pd.DataFrame()
df2 = pd.DataFrame()
today = dt.datetime.now().date().strftime("%Y")
start_date = st.date_input("Pick a start date")
stop_date = st.date_input("Pick a stop date")
for crypto in crypto_list:
    if input_crypto == "See-Comparison":
        df[crypto] = yf.Ticker(crypto).history(period='1d', start=start_date, end=stop_date).Close
    else:
        crypto = input_crypto
        df[crypto] = yf.Ticker(crypto).history(period='1d', start=start_date, end=stop_date).Close
    # df2[crypto] = yf.Ticker(crypto).history(period='1d', start="2021-01-31", end="2021-12-31").Volume
st.line_chart(df)
# st.subheader("This line chart shows the projection of crypto Volume 2021")
# st.line_chart(df2)
st.markdown("##This dataframe shows the closing number of stock price from 2021-01-31 to 2021-12-31")
# st.dataframe(df)
st.dataframe(df)

st.subheader("Do you really know that blockchain is the concept behind Crpyto and it is a Hash Function!!")
st.video("hash_function.mp4")
st.markdown("""
### Credit : Lisk Youtube channel 
""")