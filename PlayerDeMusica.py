from tkinter import *
from tkinter.filedialog import *
import pygame
import os

musicaIndex=0
musicas=[]
px=55

def go(event):
    global  musicaIndex
    musicaIndex=lista.curselection()[0]
    reproduzir()

def iniciar():
    global musicas
    musicas.clear()
    if(os.path.isfile("caminhoMusicas.txt")):
        arquivo = open("caminhoMusicas.txt",'r')
        for i in arquivo:

            musicas.append(i.rstrip('\n'))
            lista.insert(END,i.split('/')[-1])  # -1 é o ultimo elemento de uma lista 
    else:
        arquivo = open("caminhoMusicas.txt",'w')
        arquivo.close()

def reproduzir():
    global  musicas,musicaIndex


    pygame.mixer.music.load(musicas[musicaIndex])
    if(not pygame.mixer.music.get_busy()):
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
def pausar():

    pygame.mixer.music.pause()
    pygame.mixer.music.get_endevent()

def proxima():
    global  musicaIndex
    musicaIndex+=1
    pygame.mixer.music.unload()
    pygame.mixer.music.load(musicas[musicaIndex])
    pygame.mixer.music.play()
def voltar():
    global musicaIndex
    musicaIndex-=1
    pygame.mixer.music.unload()
    pygame.mixer.music.load(musicas[musicaIndex])
    pygame.mixer.music.play()
def importaMusicas():
    global lista,musicas
    caminho = askdirectory() #abre o gerenciador de arquivos
    arquivos = os.listdir(caminho) # lista todos os arquivos do caminho
    musicas=[]
    for i in arquivos:
        if(i.lower().endswith('.mp3')):  # retorna verdadeiro para os arquivos que possuem essa termincação
            musicas.append(i)
    arquivo = open("caminhoMusicas.txt",'w')
    for i in musicas:
        arquivo.write(caminho+"/"+i+'\n')

    arquivo.close()
    lista.delete(first=0,last=len(musicas))

    iniciar()

janela = Tk()
pygame.init()
janela.geometry("1000x1000")

lista = Listbox(janela,selectmode=SINGLE)


lista.pack()

lista.place(width=500,height=500,y=60,x=250)
importa = Button(janela,text='IMPORTA MUSICAS', command=lambda:importaMusicas())
importa.place(width=215,height=50,x=392.5,y=0)

play = Button(janela,text='PLAY', command=lambda:reproduzir())
play.place(width=50,height=50,x=px+392.5,y=650)
pause = Button(janela,text='PAUSE', command=lambda:pausar())
pause.place(width=50,height=50,x=px*2+392.5,y=650)
pular = Button(janela,text='>>', command=lambda:proxima())
pular.place(width=50,height=50,x=px*3+392.5,y=650)
retro = Button(janela,text='<<', command=lambda:voltar())
retro.place(width=50,height=50,x=392.5,y=650)

lista.bind('<Double-1>',go)
iniciar()
janela.mainloop()