🌍 Echolang: Online Multi-Language Text-to-Speech System
📌 Project Overview

Echolang is a Python-based Multi-Language Text-to-Speech (TTS) application that allows users to convert text into speech and translate text into multiple languages before generating audio output.

The system utilizes Google Text-to-Speech (gTTS) for speech synthesis and Google Translate for real-time language translation. It provides a simple command-line interface for users to enter text, select languages, and listen to generated speech.

🚀 Features
🔊 Text-to-Speech Conversion
Convert text into natural-sounding speech.
Supports multiple languages.
Generates audio dynamically using Google Text-to-Speech.
🌐 Language Translation
Translate text into another language before speech generation.
Real-time translation using Google Translate API.
🗣️ Multi-Language Support

Supported Languages:

Language	Code
English	en
Hindi	hi
Telugu	te
Spanish	es
French	fr
🎵 Audio Playback
Automatically plays generated audio.
Temporary audio files are removed after playback.
🛠️ Technologies Used
Python
gTTS (Google Text-to-Speech)
Googletrans
Playsound
OS Module
📂 Project Workflow

User Input
↓
Language Selection
↓
Optional Translation
↓
Text Processing
↓
Google Text-to-Speech
↓
Audio Generation (.mp3)
↓
Audio Playback
↓
Temporary File Removal

📁 Project Structure
Echolang/
│
├── echolang.py
├── README.md
├── requirements.txt
└── echolang_audio.mp3 (generated temporarily)
▶️ Installation
Clone Repository
git clone https://github.com/yourusername/Echolang.git
cd Echolang
Install Required Libraries
pip install gtts
pip install googletrans==4.0.0-rc1
pip install playsound

Or install all dependencies:

pip install -r requirements.txt
▶️ Run the Application
python echolang.py
💻 Example Usage
====== Welcome to Echolang Online TTS System ======

Supported languages:
English, Hindi, Spanish, French, Telugu

Enter your text:
Hello, how are you?

Do you want to translate it to another language? (yes/no):
yes

Enter target language:
telugu

Translated Text:
హలో, మీరు ఎలా ఉన్నారు?

Audio playback finished. ✅
📊 Applications
Language Learning Systems
Accessibility Tools
Educational Platforms
Voice Assistants
Multilingual Communication
Text Reading Applications
🔮 Future Enhancements
Speech-to-Text Conversion
GUI Interface using Tkinter
Voice Selection Options
PDF/Text File Reader
Offline TTS Support
AI-Based Voice Cloning
Additional Language Support
Web-Based Deployment
👨‍💻 Author

Developed as a Python-based Multi-Language Text-to-Speech and Translation System using Google Text-to-Speech (gTTS) and Google Translate APIs.

Key Skills Demonstrated
Python Programming
Natural Language Processing (NLP)
Text-to-Speech Systems
Language Translation
API Integration
Audio Processing
Software Development
