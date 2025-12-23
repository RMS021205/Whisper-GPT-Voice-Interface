from openai import OpenAI

client = OpenAI()

def ask_gpt(user_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 한국어로 친절하게 답하는 AI 비서야."},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content.strip()
