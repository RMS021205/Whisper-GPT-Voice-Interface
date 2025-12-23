from stt import speech_to_text
from gpt_handler import ask_gpt

def main():
    user_text = speech_to_text(duration=5)

    if not user_text:
        print("⚠️ 인식된 음성이 없습니다.")
        return

    print(f"\n🙋 사용자 질문: {user_text}")

    answer = ask_gpt(user_text)
    print(f"\n🤖 GPT 답변:\n{answer}")

if __name__ == "__main__":
    main()
