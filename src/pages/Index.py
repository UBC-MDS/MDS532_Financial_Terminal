import streamlit as st
# 设置页面宽度
st.set_page_config(layout="wide")
pages = {
    "TreasuryBond":[
        st.Page("TreasuryYieldCurve.py", title="Treasury Yield Curve"),
        
    ],
    "Stock":[
        st.Page("USCompareReturn.py", title="US Compare Stock Return"),
    ]
    
}
pg = st.navigation(pages)
pg.run()
