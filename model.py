from openai import OpenAI

def chat(prompt):
    client = OpenAI(
        api_key="ddc-a4f-63601bd0246149138ab646c1dd6dbae4",
        base_url="https://api.a4f.co/v1"
    )

    response = client.chat.completions.create(
        model="provider-6/gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=50,
        stream=False
    )

    return response.choices[0].message.content

p = chat("Hello, how are you?")
print(p)