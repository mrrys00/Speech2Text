import speech_recognition as sr

listener = sr.Recognizer()
print(listener)
print(sr.Microphone().list_microphone_names())
try:
    print("listening...")
    # print(sr.Microphone().list_microphone_names())
    with sr.Microphone(device_index=2) as source:
        voice = listener.listen(source)
        print("err1")
        info = listener.recognize_google(voice)
        print("err2")
        print(info)
except:
    print("fck off")