import streamlit as st

# 设置页面标题

pages = {
    "使用说明":[st.Page("page1.py",title="说明")],
    "产能负荷率":[st.Page("page2.py",title="数据处理")]
}

pg = st.navigation(pages)

pg.run()