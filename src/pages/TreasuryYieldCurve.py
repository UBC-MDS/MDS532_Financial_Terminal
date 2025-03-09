import streamlit as st
import os
import sys
import plotly.graph_objects as go

# Add the project's root directory to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from treasury_yield import getUSTreasuryYield, getCanadaTreasuryYield, getChinaTreasuryYield

def plotTreasuryYieldFig(df):
    """
    Use Plotly to plot the U.S. Treasury yield curve
    :param df: DataFrame containing Term, Current, One Month Ago, One Year Ago
    """
    fig = go.Figure()

    # Add current yield curve
    fig.add_trace(go.Scatter(
        x=df['Term'],
        y=df['Current'],
        mode='lines+markers+text',
        name='Current',
        line=dict(width=3),
        marker=dict(size=8),
        text=df['Current'],  # Add data labels
        textposition='top center'  # Set data label position
    ))

    # Add one month ago yield curve (default hidden)
    fig.add_trace(go.Scatter(
        x=df['Term'],
        y=df['One Month Ago'],
        mode='lines+markers+text',
        name='One Month Ago',
        line=dict(width=2, dash='dash'),
        marker=dict(size=6),
        visible='legendonly',  # Default hidden
        text=df['One Month Ago'],  # Add data labels
        textposition='top center'  # Set data label position
    ))

    # Add one year ago yield curve (default hidden)
    fig.add_trace(go.Scatter(
        x=df['Term'],
        y=df['One Year Ago'],
        mode='lines+markers+text',
        name='One Year Ago',
        line=dict(width=2, dash='dot'),
        marker=dict(size=6),
        visible='legendonly',  # Default hidden
        text=df['One Year Ago'],  # Add data labels
        textposition='top center'  # Set data label position
    ))

    # Set chart style
    fig.update_layout(
        title=f"{selected_country} Treasury Yield Curve",
        xaxis=dict(title="Term", type='category', fixedrange=True),
        yaxis=dict(title="Yield (%)", tickformat=".3f", fixedrange=True),
        template="plotly_white",
        legend=dict(orientation="h", x=0.5, y=1.2, xanchor="center"),
        hovermode="x unified",
        height=500,  # Set chart height
        dragmode=False  # Disable dragging
    )
    
    return fig

# Set Streamlit app title
st.title("Treasury Yield Curve")

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    # Add a dropdown menu for country selection
    selected_country = st.selectbox("Please select a country", ["United States", "Canada", "China"])

if selected_country == "United States":
    df = getUSTreasuryYield()
elif selected_country == "Canada":
    df = getCanadaTreasuryYield()
elif selected_country == "China":
    df = getChinaTreasuryYield()

fig = plotTreasuryYieldFig(df)
# Display chart
st.plotly_chart(fig)
# Display statistics
st.dataframe(df, use_container_width=True, height=min(df.shape[0],20)*35+40, hide_index=True)