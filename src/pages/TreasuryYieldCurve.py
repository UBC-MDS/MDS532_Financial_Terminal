import streamlit as st
import os
import sys
import plotly.graph_objects as go

# 将项目的根目录添加到 Python 的模块搜索路径中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from treasury_yield import getUSTreasuryYield, getCanadaTreasuryYield, getChinaTreasuryYield


def plotTreasuryYieldFig(df):
    """
    使用 Plotly 绘制 U.S. 国债收益率曲线
    :param df: 包含 Term, Current, One Month Ago, One Year Ago 的 DataFrame
    """
    fig = go.Figure()

    # 添加当前收益率曲线
    fig.add_trace(go.Scatter(
        x=df['Term'],
        y=df['Current'],
        mode='lines+markers+text',
        name='Current',
        line=dict(width=3),
        marker=dict(size=8),
        text=df['Current'],  # 添加数据标签
        textposition='top center'  # 设置数据标签位置
    ))

    # 添加一个月前收益率曲线（默认隐藏）
    fig.add_trace(go.Scatter(
        x=df['Term'],
        y=df['One Month Ago'],
        mode='lines+markers+text',
        name='One Month Ago',
        line=dict(width=2, dash='dash'),
        marker=dict(size=6),
        visible='legendonly',  # 默认隐藏
        text=df['One Month Ago'],  # 添加数据标签
        textposition='top center'  # 设置数据标签位置
    ))

    # 添加一年前收益率曲线（默认隐藏）
    fig.add_trace(go.Scatter(
        x=df['Term'],
        y=df['One Year Ago'],
        mode='lines+markers+text',
        name='One Year Ago',
        line=dict(width=2, dash='dot'),
        marker=dict(size=6),
        visible='legendonly',  # 默认隐藏
        text=df['One Year Ago'],  # 添加数据标签
        textposition='top center'  # 设置数据标签位置
    ))

    # 设置图表样式
    fig.update_layout(
        title=f"{selected_country} Treasury Yield Curve",
        xaxis=dict(title="Term", type='category', fixedrange=True),
        yaxis=dict(title="Yield (%)", tickformat=".3f", fixedrange=True),
        template="plotly_white",
        legend=dict(orientation="h", x=0.5, y = 1.2, xanchor="center"),
        hovermode="x unified",
        height=500,  # 设置图表高度
        dragmode=False  # 禁止拖动
    )
    
    return fig

# 设置 Streamlit 应用标题
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
# 展示图形
st.plotly_chart(fig)
# 打印统计信息
st.dataframe(df, use_container_width=True, height=min(df.shape[0],20)*35+40, hide_index=True)