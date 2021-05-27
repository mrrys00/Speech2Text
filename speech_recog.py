import speech_recognition as sr

listener = sr.Recognizer()
print(listener)
try:
    print("listening...")
    with sr.Microphone() as source:
        voice = listener.listen(source)
        print("err1")
        info = listener.recognize_google(voice)
        print("err2")
        print(info)
except:
    print("fck off")