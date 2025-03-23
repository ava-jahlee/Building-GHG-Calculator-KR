import streamlit as st

def sidebar_nav():
    with st.sidebar:
        st.markdown("### 📌 메뉴")
        if st.button("🏠 메인으로"):
            st.session_state.menu = "메인"
        if st.button("📊 온실가스 배출량 계산기"):
            st.session_state.menu = "계산기"
        if st.button("📈 매개변수 데이터"):
            st.session_state.menu = "매개변수"
        if st.button("📋 관리기준"):
            st.session_state.menu = "관리기준"
