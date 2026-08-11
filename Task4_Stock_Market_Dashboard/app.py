import streamlit as st
import requests
import pandas as pd
import plotly.express as px


st.title("📈 Stock Market Dashboard")


st.sidebar.header("Dashboard Settings")
st.sidebar.write("Select a stock and time period to view its market data.")

stock = st.sidebar.selectbox(
    "Choose a stock:",
    ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
)

period = st.sidebar.selectbox(
    "Select time period:",
    ["1 Month", "3 Months", "6 Months", "1 Year"]
)



if period == "1 Month":
    range_value = "1mo"
elif period == "3 Months":
    range_value = "3mo"
elif period == "6 Months":
    range_value = "6mo"
else:
    range_value = "1y"

url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock}?range={range_value}&interval=1d"


headers = {"User-Agent": "Mozilla/5.0"}



response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    result = data["chart"]["result"][0]
    meta = result["meta"]

    price = meta["regularMarketPrice"]
    high = meta["regularMarketDayHigh"]
    low = meta["regularMarketDayLow"]
    volume = meta["regularMarketVolume"]
    company = meta["longName"]


    timestamps = result["timestamp"]
    prices = result["indicators"]["quote"][0]["close"]

    df = pd.DataFrame({
        "Date": pd.to_datetime(timestamps, unit="s"),
        "Closing Price": prices
    })
    
    df = df.dropna()

    first_price = prices[0]
    change_percent = ((price - first_price) / first_price) * 100

    st.subheader(company)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Current Price", f"${price:.2f}", f"{change_percent:+.2f}%")
    col2.metric("Day High", f"${high}")
    col3.metric("Day Low", f"${low}")
    col4.metric("Volume", f"{volume:,}")

    
    fig = px.line(
        df,
        x="Date",
        y="Closing Price",
        title=f"{company} - {period}"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Unable to fetch stock data.")
  
