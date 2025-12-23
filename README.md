# 🎤 Voice GPT Assistant

## 📌 Overview
Voice GPT Assistant는 노트북 마이크로 입력된 사용자의 음성을  
Whisper 기반 STT(Speech-to-Text)로 텍스트로 변환하고,  
변환된 텍스트를 GPT API에 전달하여  
자연어 텍스트 응답을 출력하는 음성 기반 AI 질의 시스템입니다.

---

## 🧠 System Flow
User Voice  
→ Notebook Microphone  
→ Whisper STT  
→ Text Question  
→ GPT API  
→ Text Response (Terminal)

---

## ✨ Features
- 노트북 내장 마이크 음성 입력
- Whisper 기반 한국어 음성 인식(STT)
- GPT API 연동 텍스트 질의 응답
- 무음 입력 예외 처리
- 마이크 장치 목록 조회 기능 포함

---

## 🛠 Tech Stack
- Python 3.10+
- OpenAI Whisper
- OpenAI GPT API
- sounddevice
- NumPy
- FFmpeg (Windows 환경 필수)

---

## 📁 Project Structure
voice_gpt/
├─ main.py # 전체 실행 흐름 제어
├─ stt.py # 음성 → 텍스트(STT)
├─ gpt_handler.py # GPT 질의 처리
├─ list_devices.py # 마이크/오디오 장치 목록 조회
├─ venv/ # Python 가상환경 (gitignore)

yaml
코드 복사

---

## ⚙️ Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-id/voice-gpt.git
cd voice-gpt
2. Create Virtual Environment
bash
코드 복사
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
bash
코드 복사
pip install -r requirements.txt
4. Set OpenAI API Key
bash
코드 복사
setx OPENAI_API_KEY "YOUR_API_KEY"
5. (Optional) Check Audio Devices
bash
코드 복사
python list_devices.py
6. Run
bash
코드 복사
python main.py

▶️ Example Output

🎤 말하세요...
📝 인식된 텍스트: 축가 추천해줘

🙋 사용자 질문: 축가 추천해줘

🤖 GPT 답변:
결혼식 축가로는 ...

🚀 Future Improvements
GPT 응답 음성 출력(TTS)

지속 대화 기능

외부 API 연동

로봇 제어 명령 연동
