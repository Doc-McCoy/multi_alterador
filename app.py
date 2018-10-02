#!python3
import os
from tkinter import *
from tkinter import filedialog

class App:

    def __init__(self, root):
        
        root.title("Multi alterador.")
        root.resizable(0,0)

        self.frameMain = Frame(root)
        self.frameMain.pack()

        # Path
        self.framePath = Frame(self.frameMain)
        self.framePath.pack()
        self.labelPath = Label(self.framePath, text="Pasta: ")
        self.labelPath.pack(side=LEFT)
        self.inputPath = Entry(self.framePath, width=50)
        self.inputPath.pack(side=LEFT)
        self.buttonPath = Button(self.framePath, text="Abrir", command=self.setPath)
        self.buttonPath.pack(side=LEFT)

        # Texto
        self.frameText = Frame(self.frameMain)
        self.frameText.pack()
        self.labelText = Label(self.frameText, text="Digite o texto a ser adicionado:")
        self.labelText.pack()
        self.areaText = Text(self.frameText, height=10, width=60)
        self.areaText.pack()

    def setPath(self):
        """ Pergunta ao usuário a pasta que será modificada e salva o caminho na variável 'path'. """
        self.path = filedialog.askdirectory(title="Selecione a pasta onde os arquivos estão")
        self.inputPath.insert(0, self.path)

    def setFilesName(self):
        """ Cria uma lista com os arquivos que estão na pasta na pasta. """
        self.files = os.listdir(self.path)

    def modifuFiles(self):
        """ Modifica todos os arquivos em self.files e adiciona o que está no self.text """
        pass

    """
    for file in files:

        fileOpen = open(file, "r+")
        content = arquivo.readlines()
        content.insert(0, texto)

        fileOpen.seek(0,0)
        fileOpen.writelines(content)
        fileOpen.close()
    """


if __name__ == '__main__':
    root = Tk()
    App(root)
    root.mainloop()