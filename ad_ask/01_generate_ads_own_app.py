import streamlit as st
import openai

def askGpt(prompt, apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse

def main():
    st.set_page_config(page_icon="📣",page_title="광고 문구 생성 프로그램")
    # session_state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPEN_API"] = ""

    #사이드바
    with st.sidebar:
        open_apikey = st.text_input(label="OpenAI API key",placeholder="API키 입력",value="",type="password")
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown("---")
    
    #메인공간
    st.header("📣광고 문구 생성 프로그램📣")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("제품명",placeholder="")
        strenghth = st.text_input("제품 특징",placeholder="")
        keyword = st.text_input("필수 포함 키워드",placeholder="")
        cost = st.text_input("가격")
    with col2:
        com_name = st.text_input("회사명",placeholder="구글,삼성")
        tone_manner = st.text_input("톤엔 메너",placeholder="감성적이게, 발랄하게")
        value = st.text_input("브랜드 핵심 가치",placeholder="선택사항")

    if st.button("광고 문구 생성"):
        prompt = f'''
        아래의 내용을 참고해서 1~2줄짜리 광고문구 5개를 작성해줘
        - 제품명: {name}
        - 회사명: {com_name}
        - 제품 특징: {strenghth}
        - 톤엔 메너: {tone_manner}
        - 필수 포함 키워드: {keyword}
        - 브랜드 핵심 가치: {value}
        - 가격: {cost}
        '''
        st.info(askGpt(prompt,st.session_state["OPENAI_API"]))

if __name__=="__main__":
    main()