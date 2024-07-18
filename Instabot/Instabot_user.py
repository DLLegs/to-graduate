import streamlit as st
import openai
from instagrapi import Client
from PIL import Image
import urllib
from googletrans import Translator

#### 함수 ####
#영어로 번역
def google_trans(messages):
    google = Translator()
    result = google.translate(messages, date="en")
    return result.text

#인스타 업로드
def uploadinstagram(description):
    cl = Client()
    cl.login(st.session_state["instagram_ID"], st.session_state["instagram_Password"])
    cl.photo_upload("instaimg_resize.jpg", description)

#GPT에게 질문/답변받기
def getdescriptionFromGPT(topic, mood, apikey):
    prompt = f'''
Write me the Instagram post description or caption in just a few sentences for the post 
-topic : {topic}
-Mood : {mood}
Format every new sentence with new lines so the text is more readable.
Include emojis and the best Instagram hashtags for that post.
The first caption sentence should hook the readers.
write all output in korean.'''
    messages_prompt = [{"role": "user", "content": prompt}]
    
    openai.api_key = apikey
    # openai_client = openai.OpenAI(api_key=apikey) 객체 생성이 필요한 경우
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_prompt
    )
    gptResponse = response.choices[0].message['content']
    return gptResponse

#DALLE.2에게 질문/그림 URL 받기
def getImageURLFromDALLE(topic, mood, apikey):
    t_topic = google_trans(topic)
    t_mood = google_trans(mood)
    prompt=f'Draw picture about {t_topic}. picture mood is {t_mood}'
    openai.api_key = apikey
    response = openai.Image.create(
        model="dall-e-2",
        prompt=prompt,
        size="512x512",
        n=1,
    )
    image_url = response.data[0].url
    urllib.request.urlretrieve(image_url, "instaimg.jpg")

### 메인 함수 ###
def main():
    st.set_page_config(page_title="Instabot", page_icon="📷")

    # session state 초기화
    if "description" not in st.session_state:
        st.session_state["description"] = ""
    
    if "flag" not in st.session_state:
        st.session_state["flag"] = False
    
    if "instagram_ID" not in st.session_state:
        st.session_state["instagram_ID"] = ""
    
    if "instagram_Password" not in st.session_state:
        st.session_state["instagram_Password"] = ""
    
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
    
    # 제목
    st.header('instagram 포스팅 생성기')
    st.markdown('---')

    # 설명란
    with st.expander("인스타그램 포스팅 생성기", expanded=True):
        st.write(
            """
            - 인스타그램 포스팅 생성는 UI는 스트림릿을 활용하여 만들었습니다.
            - 이미지는 OpenAI의 Dall.e 2 를 활용하여 생성합니다. 
            - 포스팅 글은 OpenAI의 GPT 모델을 활용하여 생성합니다. 
            - 자동 포스팅은 instagram API를 활용합니다.
            """

        )
        st.markdown("")

    with st.sidebar:
        open_apikey = st.text_input(label='OPENAI API키', placeholder='API키를 입력하시오', value='', type='password')

        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        
        st.markdown('---')

    topic = st.text_input(label="주제", placeholder="축구, 인공지능, 옥수수...")
    mood = st.text_input(label="분위기",placeholder="재미있는, 진지한, 우울한...")

    if st.button(label="생성", type="secondary") and not st.session_state["flag"]:
        with st.spinner('생성중'):
            st.session_state["description"] = getdescriptionFromGPT(topic, mood, st.session_state["OPENAI_API"])
            getImageURLFromDALLE(topic, mood, st.session_state["OPENAI_API"])
            st.session_state["flag"] = True
        
    if st.session_state["flag"]:
        image = Image.open('instaimg.jpg')
        st.image(image)
        txt = st.text_area(label="Edit Description", value=st.session_state["description"], height=50)
        st.session_state["description"] = txt

        st.markdown('인스타그램 ID/PW')
        st.session_state["instagram_ID"] = st.text_input(label="인스타그램 아이디", value='')
        st.session_state["instagram_Password"] = st.text_input(label="인스타그램 비밀번호", type='password', value='')

        if st.button(label="업로드"):
            image = Image.open("instaimg.jpg")
            image = image.convert("RGB")
            new_image = image.resize((1080, 1080))
            new_image.save("instaimg_resize.jpg")
            uploadinstagram(st.session_state['description'])
            st.session_state['flag'] = False

if __name__ == "__main__":
    main()
