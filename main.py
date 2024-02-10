import speech_recognition as sr

def reconhecer_fala():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        try:
            audio = microfone.listen(source)
            frase = microfone.recognize_google(audio, language='pt-BR')
            print("Você disse: " + frase)
        except sr.UnknownValueError:
            print("Não foi possível entender o que você disse!")
            return ""  # Return an empty string in case of recognition failure
        except sr.RequestError as e:
            print(f"Erro na requisição ao Google API: {e}")
            return ""  # Return an empty string in case of API request error

        return frase

def transcresver_arquivo_txt(frase):
    try:
        with open('transcricao.txt', 'w') as arquivo:
            arquivo.write(frase)
        print('A transcrição foi salva com sucesso!')
    except IOError as e:
        print(f'Erro ao escrever no arquivo: {e}')

frase_reconhecida = reconhecer_fala()
transcresver_arquivo_txt(frase_reconhecida)
