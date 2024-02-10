import speech_recognition as sr
from tkinter import *

def iniciar_gravacao():
    global texto_transcricao
    texto_transcricao = "Transcrevendo ..."
    orientacao3['text'] = texto_transcricao
    play['state'] = 'disabled' # Desabilita o botão "Play" durante a gravação
    stop['state'] = 'normal' # Habilita o botão "Stop"

    global microfone
    microfone = sr.Recognizer() # Habilita o microfone
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) # Redução de ruído disponível na speech_recognition
        print("Diga alguma coisa: ")
        audio = microfone.listen(source, timeout=0) # Guarda o áudio falado na variável 'audio'; o áudio não é finalizado por timeout
        try:
            frase = microfone.recognize_google(audio, language='pt-BR') # O áudio será interpretado na língua portuguesa
            print("Você disse: " + frase)
            texto_transcricao = "A transcrição foi finalizada."
        except:
            print("Não entendi o que você disse!")
            texto_transcricao = "Erro na transcrição"

        orientacao3['text'] = texto_transcricao
        play['state'] = 'normal' # Habilita novamente o botão "Play"

def transcresver_arquivo_txt():
    try:
        with open('transcricao.txt', 'w') as arquivo:
            arquivo.write(frase)
        print('A transcrição foi salva com sucesso!')
    except IOError:
        print('Ocorreu um erro ao salvar a transcrição!')

janela = Tk()
janela.title('Transcrever Áudios em Texto')

orientacao1 = Label(janela, text='Iniciar')
orientacao1.grid(column=0, row=0)

play = Button(janela, text='Play ▶', command=iniciar_gravacao)
play.grid(column=0, row=1)

orientacao2 = Label(janela, text='Parar e Salvar')
orientacao2.grid(column=0, row=2)

stop = Button(janela, text='Stop ■', command=janela.quit, state='disabled') # Altera o comando do botão Stop para sair da aplicação e inicialmente desabilitado
stop.grid(column=0, row=3)

texto_transcricao = "A transcrição foi finalizada."
orientacao3 = Label(janela, text=texto_transcricao)
orientacao3.grid(column=0, row=4)

janela.mainloop()
