import streamlit as st
import pandas as pd
import nav
import import_data as ipt

st.set_page_config(page_title="GHG Calculator", layout="wide")
nav.sidebar_nav()

# 메뉴 선택
menu = st.session_state.get("menu", "메인")

if menu == "메인":
    st.title("🏢 건축물 온실가스 계산기 (GHG Calculator)")
    st.markdown("**IPCC 2006 GL 에너지 1A4a・1A4b**")

elif menu == "계산기":
    st.title("📊 온실가스 배출량 계산기")
    # 계산기 내용

elif menu == "매개변수":
    st.title("📈 매개변수 데이터")
    
    tab1_titles="배출계수", "열량계수", "산화계수", "지구온난화계수"
    tabs1 = st.tabs(tab1_titles)
    with tabs1[0]: #배출계수
        st.subheader("**🌵Tier1🌵**") 
        st.caption('''<div style='text-align: right;'> IPCC 2006, 단위 : kgGHG/TJ 또는 kgGHG/MWh </div>''',
                        unsafe_allow_html=True)
        
        df_배출계수T1 = pd.DataFrame(pd.read_excel(ipt.info_data, sheet_name='배출계수_T1', header=1))
        fuel_group = ["석유류", "석탄류", "가스류", "기타 화석연료 및 바이오매스", "전력 및 열(스팀)"]  
        with st.expander("**IPCC 06 기준 배출계수**"):
            연료분류 = st.selectbox('IPCC 분류', fuel_group)
            if 연료분류 == "석유류":
                df_배출계수T1_석유류 = df_배출계수T1.iloc[:28, 1:6]
                st.dataframe(df_배출계수T1_석유류, hide_index=True)
            elif 연료분류 == "석탄류":
                df_배출계수T1_석탄류 = df_배출계수T1.iloc[28:41, 1:6]
                st.dataframe(df_배출계수T1_석탄류, hide_index=True)
            elif 연료분류 == "가스류":
                df_배출계수T1_가스류 = df_배출계수T1.iloc[41:48, 1:6]
                st.dataframe(df_배출계수T1_가스류, hide_index=True)
            elif 연료분류 == "기타 화석연료 및 바이오매스":
                df_배출계수T1_기타류 = df_배출계수T1.iloc[48:63, 1:6]
                st.dataframe(df_배출계수T1_기타류, hide_index=True)
            elif 연료분류 == "전력 및 열(스팀)":
                df_배출계수T1_전력열 = df_배출계수T1.iloc[63:, 1:6]
                st.dataframe(df_배출계수T1_전력열, hide_index=True)

        st.divider()
        
        st.subheader("**🌵Tier2🌵**")
        st.caption('''<div style='text-align: right;'> 온실가스종합정보센터(GIR), 단위 : kgGHG/TJ 또는 kgGHG/MWh </div>''',
                    unsafe_allow_html=True) 
        st.info('''**🫱🏻‍🫲🏻국가 고유 온실가스 배출계수**
                \n * 국가고유(17년): 제 7차 개정('11~'15년 유통 시료)
                \n * 국가고유(22년): 제 8차 개정('16~'20년 유통 시료)''')
        
        schedule_국가고유 = st.radio(label='', options=('국가고유(17년)', '국가고유(22년)'))
        if schedule_국가고유 == '국가고유(17년)':
            df_배출계수T2 = pd.DataFrame(pd.read_excel(ipt.info_data, sheet_name='배출계수_T2_17', header=1))
        elif schedule_국가고유 == '국가고유(22년)':
            df_배출계수T2 = pd.DataFrame(pd.read_excel(ipt.info_data, sheet_name='배출계수_T2_22', header=1))

        with st.expander("**온실가스종합정보센터(GIR) 기준 배출계수**"):
            연료분류2 = st.selectbox('국가고유 분류', fuel_group)
            if 연료분류2 == "석유류":
                df_배출계수T2_석유류 = df_배출계수T2.iloc[:28, 1:7]
                st.dataframe(df_배출계수T2_석유류, hide_index=True)
            elif 연료분류2 == "석탄류":
                df_배출계수T2_석탄류 = df_배출계수T2.iloc[28:41, 1:7]
                st.dataframe(df_배출계수T2_석탄류, hide_index=True)
            elif 연료분류2 == "가스류":
                df_배출계수T2_가스류 = df_배출계수T2.iloc[41:48, 1:7]
                st.dataframe(df_배출계수T2_가스류, hide_index=True)
            elif 연료분류2 == "기타 화석연료 및 바이오매스":
                df_배출계수T2_기타류 = df_배출계수T2.iloc[48:63, 1:7]
                st.dataframe(df_배출계수T2_기타류, hide_index=True)
            elif 연료분류2 == "전력 및 열(스팀)":
                df_배출계수T2_전력열 = df_배출계수T2.iloc[63:, 1:7]
                st.dataframe(df_배출계수T2_전력열, hide_index=True)

        st.divider()

        st.subheader("**🌵Tier3🌵**")
        st.info('''**🫱🏻‍🫲🏻온실가스 배출권 거래제 계획기간**
                \n * 3기: 제3차(2021 ~ 2025)
                \n * 4기: 제4차(2026 ~ 2030)
                \n *수도권지사: 파주, 삼송, 고양, 중앙, 강남, 판교, 분당, 용인, 광교, 수원, 화성, 동탄)*''')               

        with st.expander("**한국지역난방공사_열(스팀)**"):
            trade_schedule = ['3기', '4기']
            계획기간 = st.selectbox('계획기간', trade_schedule)
            df_한국지역난방공사배출계수 = pd.DataFrame(pd.read_excel(ipt.info_data,sheet_name='열배출계수_한국지역난방공사',header=1))
            st.caption('''<div style='text-align: right;'> 단위: kgGHG/TJ </div>''',
                            unsafe_allow_html=True)
            
            if 계획기간 == '3기':
                df_한국지역난방공사배출계수3 = df_한국지역난방공사배출계수.iloc[:8,1:5]
                st.dataframe(df_한국지역난방공사배출계수3.fillna("-"), hide_index=True)
            elif 계획기간 == '4기':
                df_한국지역난방공사배출계수4 = df_한국지역난방공사배출계수.iloc[8:,1:5]
                st.dataframe(df_한국지역난방공사배출계수4.fillna("-"), hide_index=True)

    with tabs1[1]:
        st.subheader("**🌵Tier1🌵**") 
        st.subheader("**🌵Tier2🌵**")

    with tabs1[2]:
        st.subheader("**🌵Tier1🌵**")
        with st.expander("**산화계수 기본값**"):
            df_연료상태_T1 = pd.DataFrame({'value': [1.0, 1.0, 1.0]}, index=['고체', '액체', '기체'])
            st.dataframe(df_연료상태_T1)

        st.subheader("**🌵Tier2🌵**")
        with st.expander("**산화계수**"):
            select_산화계수 = st.selectbox('연료상태 및 값', ['연료상태(상온)', '값'])
            st.caption('''<div style='text-align: right;'> 단위: - </div>''',
                            unsafe_allow_html=True)
            df_연료상태_T2 = pd.DataFrame(pd.read_excel(ipt.info_data, sheet_name="산화계수", header=1))

            if select_산화계수 == '연료상태(상온)':
                df_연료상태_T2 = df_연료상태_T2.iloc[0:, 0:3]
                st.dataframe(df_연료상태_T2)
            elif select_산화계수 == '값':
                df_연료상태_T2 = df_연료상태_T2.iloc[0:3, 5:]
                st.dataframe(df_연료상태_T2)


elif menu == "관리기준":
    st.title("📋 관리기준")
    st.subheader("2. 관리기준 *")
    st.markdown("***출처: 배출활동별, 시설규모별 산정등급(Tier) 최소적용기준**")

    st.markdown("**📍 시설규모 기준**")
    df_시설규모 = pd.DataFrame(pd.read_excel(ipt.info_data,
                                            sheet_name='관리기준',
                                            header=0))       
    df_시설규모 = df_시설규모.iloc[:3,:3]                               
    st.dataframe(df_시설규모, hide_index=True)

    st.markdown("**📍 고정연소 배출활동**")
    df_고정연소배출활동 = pd.DataFrame(pd.read_excel(ipt.info_data,
                                        sheet_name='관리기준',
                                        header=[5,6]
                                        ))       
    df_고정연소배출활동 = df_고정연소배출활동.iloc[:3,:]                               
    st.dataframe(df_고정연소배출활동, hide_index=True)

    st.markdown("**📍 이동연소 배출활동**")
    df_이동연소배출활동 = pd.DataFrame(pd.read_excel(ipt.info_data,
                                        sheet_name='관리기준',
                                        header=[11,12]
                                        ))       
    df_이동연소배출활동 = df_이동연소배출활동.iloc[:4,:13]                               
    st.dataframe(df_이동연소배출활동, hide_index=True)

    
    st.markdown("**📍 전기/열 배출활동**")
    df_전기열배출활동 = pd.DataFrame(pd.read_excel(ipt.info_data,
                                        sheet_name='관리기준',
                                        header=[18,19]
                                        ))       
    df_전기열배출활동 = df_전기열배출활동.iloc[:3,:10]                               
    st.dataframe(df_전기열배출활동, hide_index=True)
