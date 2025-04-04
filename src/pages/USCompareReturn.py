import streamlit as st
import pandas as pd
import os
import sys
import time
import datetime
import pytz

# Add the project's root directory to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from plot import getUSCompareReturnFig

st.title("US Compare Stock Return")
# Use Streamlit input boxes to get stock tickers
col1, col2, col3 = st.columns([1,1,5])

with col1:
    start_date = st.text_input("Start Date:", '2024-03-01')
with col2:
    today = datetime.datetime.now(pytz.timezone('America/New_York')).date().strftime('%Y-%m-%d')
    end_date = st.text_input("End Date:", today)
with col3:
    tickers_input = st.text_input("Tickers:", 'AAPL, MSFT, NVDA')
    ticker_list = [ticker.strip() for ticker in tickers_input.split(',') if ticker.strip()]
st.text("Ticker Examples: AAPL: Apple Inc.   MSFT: Microsoft Corp.   NVDA: NVIDIA Corp.    KO: Coca-Cola Co.   TSLA: Tesla Inc.  VOO: Vanguard S&P 500 ETF")

@st.cache_data(ttl=1)
def refresh_data():
    fig, df, stats_df = getUSCompareReturnFig(ticker_list, start_date, end_date)
    st.plotly_chart(fig)
    # Display statistics
    styled_stats_df = (
        stats_df.style.format({
            'Return': '{:.2%}',
            'AnnualizedReturn': '{:.2%}',
            'MaxDrawdown': '{:.2%}',
            'Calmar': '{:.2f}',
            'AnnualizedVolatility': '{:.2%}',
            'Sharpe': '{:.2f}',
        })
    )
    st.dataframe(styled_stats_df, use_container_width=True, height=stats_df.shape[0]*35+40, hide_index=True)
    st.subheader("Data")
    st.dataframe(df, use_container_width=True, height=min(df.shape[0], 10)*35+40, hide_index=True)

refresh_data()



