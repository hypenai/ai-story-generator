from gtts import gTTS

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
