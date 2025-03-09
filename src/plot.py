import numpy as np
import pandas as pd
import plotly.graph_objects as go
from xueqiu_data import getUSStockHistoryByDate
import datetime
import pytz

def getUSCompareReturnFig(ticker_list, start_date, end_date, title='Compare Return'):
    fig_height = 500
    fig = go.Figure()

    combined_df = None
    statistics = []  # To store statistics

    for ticker in ticker_list:
        df = getUSStockHistoryByDate(ticker, start_date, end_date)
        df['Return'] = df['close'] / df['close'].iloc[0] - 1
        
        texts = [""] * len(df['Timestamp_str'])
        texts[-1] = f"{ticker}: {df['Return'].iloc[-1]:.2%}"
        fig.add_trace(
            go.Scatter(
                x=df['Timestamp_str'],
                y=df['Return'],
                mode='lines+text',  # Display lines, points, and text
                text=texts,
                textposition='middle right',
                marker=dict(size=6),
                name=ticker,
                #hovertext=ticker,
                cliponaxis=False,
            )
        )
        
        # Merge data by date
        df_subset = df[['Timestamp_str', 'close', 'Return']].copy()
        df_subset = df_subset.rename(columns={
            'close': f'{ticker}_Close',
            'Return': f'{ticker}_Return'
        })
        if combined_df is None:
            combined_df = df_subset
        else:
            combined_df = pd.merge(combined_df, df_subset, on='Timestamp_str', how='outer')
        
        # Calculate statistics
        total_return = df['Return'].iloc[-1]
        # Maximum drawdown
        df['cummax'] = df['close'].cummax()
        df['drawdown'] = df['close'] / df['cummax'] - 1
        max_drawdown = abs(df['drawdown'].min())
        # Daily return and its standard deviation
        df['daily_return'] = df['close'].pct_change()
        std_daily = df['daily_return'].std()
        sharpe = (df['daily_return'].mean() / std_daily) * np.sqrt(252) if std_daily != 0 else np.nan
        # Annualized volatility
        annual_volatility = std_daily * np.sqrt(252)

        # New: Calculate annualized return
        n_days = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days
        annualized_return = (1+total_return)**(365 / n_days) - 1 if n_days > 0 else np.nan
        calmar = annualized_return / max_drawdown if max_drawdown != 0 else np.nan
        
        statistics.append({
            'Ticker': ticker,
            'Return': total_return,
            'AnnualizedReturn': annualized_return,
            'MaxDrawdown': max_drawdown,
            'Calmar': calmar,
            'AnnualizedVolatility': annual_volatility,
            'Sharpe': sharpe,
        })
    statistics_df = pd.DataFrame(statistics)
    
    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Return',
        hovermode='x unified',
        template='plotly_white',
        height=fig_height,
        margin=dict(l=40, r=140, t=80, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    fig.update_xaxes(
        tickformat="%Y-%m-%d",
        range=[start_date, end_date]
    )
    fig.update_yaxes(title_text="Return", tickformat=".2%", fixedrange=True)
    
    return fig, combined_df, statistics_df

if __name__=="__main__":
    start_date = '2022-01-01'
    end_date = datetime.datetime.now(pytz.timezone('America/New_York')).date().strftime('%Y-%m-%d')
    ticker_list = ['QQQ', 'SGOV']

    fig, df, stats_df = getUSCompareReturnFig(ticker_list, start_date, end_date)
    fig.show()
    print(stats_df)
