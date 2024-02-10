from tkinter import *

janela = Tk()
janela.title('Transcrever Áudios em Texto')

orientacao1 = Label(janela, text='Iniciar')
orientacao1.grid(column=0, row=0)

play = Button(janela, text='Play ▶', command='#')
play.grid(column=0, row=1)

orientacao2 = Label(janela, text='Parar e Salvar')
orientacao2.grid(column=0, row=2)

stop = Button(janela, text='Stop ■', command='#')
stop.grid(column=0, row=3)

texto1 = 'Transcrevendo'
texto2 = 'Transcrição interrompida e salva'

orientacao3 = Label(janela, text='')
orientacao3.grid(column=0, row=4)
orientacao3['text'] = texto1
orientacao3['text'] = texto2

janela.mainloop()