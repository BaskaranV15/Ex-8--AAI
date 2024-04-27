import speech_recognition as sr
# initialize the reconizer
r=sr.Recognizer()
# set duration for the audio
duration=15 # second=
# record audio
print("say somthing:")

with sr.Microphone() as source:
    audio_date=r.listen(source,timeout=duration)
try:
    text=r.recognize_google(audio_date)
    print("you said:",text)
except sr.UnknownValueError:
    print("sorry ,could not undersand audio")
except sr.RequestError as e:
    print(f'Error with the request to google speech recognation service:{e}')
except Exception as e:
    print(f'Error:{e}') 