# ==========================================
# Echolang: Online Multi-Language Text-to-Speech
# Supports: English, Hindi, Telugu, Spanish, French
# ==========================================

from gtts import gTTS
from googletrans import Translator
from playsound import playsound
import os

# Initialize translator
translator = Translator()

# Supported languages for gTTS and translation
supported_languages = {
    'english': 'en',
    'hindi': 'hi',
    'spanish': 'es',
    'french': 'fr',
    'telugu': 'te'
}

# Function: Text-to-Speech
def speak_text(text, language='english'):
    language = language.lower()
    if language not in supported_languages:
        print(f"Error: {language} not supported!")
        return

    tts = gTTS(text=text, lang=supported_languages[language])
    audio_file = "echolang_audio.mp3"
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)

# Function: Translate text
def translate_text(text, target_language='english'):
    target_language = target_language.lower()
    if target_language not in supported_languages:
        print(f"Error: {target_language} not supported!")
        return text
    translated = translator.translate(text, dest=supported_languages[target_language])
    return translated.text

# ===========================
# MAIN PROGRAM
# ===========================
print("====== Welcome to Echolang Online TTS System ======")
print("Supported languages: English, Hindi, Spanish, French, Telugu")

# Input text
text_input = input("Enter your text: ")

# Translate choice
translate_choice = input("Do you want to translate it to another language? (yes/no): ").strip().lower()

if translate_choice == 'yes':
    target_lang = input("Enter target language (english, hindi, spanish, french, telugu): ").strip().lower()
    final_text = translate_text(text_input, target_lang)
    print(f"Translated Text: {final_text}")
    speak_text(final_text, target_lang)
else:
    target_lang = input("Enter language for speech output (english, hindi, spanish, french, telugu): ").strip().lower()
    speak_text(text_input, target_lang)

print("Audio playback finished. ✅")

