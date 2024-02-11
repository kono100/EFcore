import speech_recognition as sr
from tkinter import *
import threading

frase = ""

def reconhecer_fala():
    global frase
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        try:
            audio = microfone.listen(source, timeout=10)  # Defina um timeout adequado
            frase = microfone.recognize_google(audio, language='pt-BR')
            print("Você disse: " + frase)
        except sr.WaitTimeoutError:
            print("Tempo de espera excedido. Tente novamente.")
        except sr.UnknownValueError:
            print("Não entendi o que você disse!")

def transcresver_arquivo_txt():
    global frase
    try:
        with open('transcricao.txt', 'w') as arquivo:
            arquivo.write(frase)
        print('A transcrição foi salva com sucesso!')
    except IOError:
        print('Fudeu, Não funcionou!')

def iniciar_thread_reconhecimento():
    thread_reconhecimento = threading.Thread(target=reconhecer_fala)
    thread_reconhecimento.start()

janela = Tk()
janela.title('Transcrever Áudios em Texto')

orientacao1 = Label(janela, text='Iniciar')
orientacao1.grid(column=0, row=0)

play = Button(janela, text='Play ▶', command=iniciar_thread_reconhecimento)
play.grid(column=0, row=1)

orientacao2 = Label(janela, text='Parar e Salvar')
orientacao2.grid(column=0, row=2)

stop = Button(janela, text='Stop ■', command=transcresver_arquivo_txt)
stop.grid(column=0, row=3)

janela.mainloop()
