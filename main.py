import speech_recognition as sr

#criando um reconhecedor
r = sr.Recognizer()

#abrir microfone  para captura
with sr.Microphone() as source:
    
    while True:
        audio = r.listen(source) #define microfone como fonte de áudio

        print(r.recognize_google(audio, language='pt'))