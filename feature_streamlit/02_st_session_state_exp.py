import streamlit as st

total = 0

num = st.text_input(" ")
if num:
    total = total+int(num)

st.title(total)

# # 코드 초기화 방지
# # streamlit은 입력값 혹은 버튼을 누를 경우
# # 코드 전체가 실행되어 초기화됨
# if "total" not in st.session_state: 
#     st.session_state["total"] = 0 # ->session_state가 없으면 생성

# num = st.text_input(" ")
# if num:
#     st.session_state["total"] = st.session_state["total"]+int(num)

# st.title(st.session_state["total"])


