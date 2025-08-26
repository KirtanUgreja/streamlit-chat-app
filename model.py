from openai import OpenAI

def chat(prompt):
    client = OpenAI(
        api_key="Your API hear", # insert your A4F API key here
        base_url="https://api.a4f.co/v1"
    )

    response = client.chat.completions.create(
        model="provider-6/gpt-4o", # replace with your model name from A4F model list
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=50,
        stream=False
    )

    return response.choices[0].message.content
