#select version
#return tokens & price

def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content, response.usage.completion_tokens,response.usage.prompt_tokens 
