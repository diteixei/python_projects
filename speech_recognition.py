import speech_recognition as speech_recognition

rec = sr.Recognizer()

#escolher o mic para ver a lista, rodar um print(sr.Microphone().list_microphone_n)
with sr.Microphone(device_index=3) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Fale alguma coisa")
    audio = rec.listen(mic)
    frase = rec.recognize_google(audio, language="pt-BR")
    print(frase)