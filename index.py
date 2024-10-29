import streamlit as st

st.title("AI大模型应用产品网")

col,col1 = st.columns(2)
with col:
    st.image("https://inews.gtimg.com/om_bt/OOVjOUN3P4PQadYlYY8n6bau18Jxz7a64RnNr8lpx_4cwAA/641",use_column_width=True)
    flag = st.button("爱说话",use_container_width=True)
    if flag:
        st.switch_page("pages/demo03.py")

with col1:
    st.image("https://inews.gtimg.com/om_bt/OOVjOUN3P4PQadYlYY8n6bau18Jxz7a64RnNr8lpx_4cwAA/641",use_column_width=True)
    flag1 = st.button("爱画图",use_container_width=True)
    if flag1:
        st.switch_page("pages/textToImage.py")
