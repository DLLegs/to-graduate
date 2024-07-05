#select version
#return tokens & price

def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content, response.usage.completion_tokens,response.usage.prompt_tokens 

#show tokens & price

st.header("ChatGPT")
        if prompt: # prompt 입력시만
            if st.session_state["OPENAI_API"]: # OPENAI_API 입력시만
                result, completion_token,prompt_token  = askGpt(prompt,st.session_state["OPENAI_API"])
                st.markdown(result)
                if st.session_state["model"] == "gpt-3.5-turbo":
                    total_bill = (completion_token*0.02+prompt_token*0.015)*0.001
                    
                    st.info(f"총 사용 토큰 : {(completion_token+prompt_token)}")
                    st.info(f"금액 : {total_bill}$")
                else:
                    total_bill = (completion_token*0.06+prompt_token*0.03)*0.001
                    
                    st.info(f"총 사용 토큰 : {(completion_token+prompt_token)}")
                    st.info(f"금액 : {total_bill}$")
            else:
                st.info("OpenAI API 키를 입력하세요")
