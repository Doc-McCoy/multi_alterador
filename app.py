#!python3
import os
from tkinter import *
from tkinter import filedialog

class App:

    def __init__(self, root):

        root.title("Multi alterador")
        root.resizable(0,0)

        # Frame raíz
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

        # Radios
        self.posicao = IntVar()
        self.frameRadios = Frame(self.frameText)
        self.frameRadios.pack(fill='x')
        self.radioA = Radiobutton(self.frameRadios, text="Adicionar ao início", variable=self.posicao, value=1)
        self.radioA.pack(side=LEFT)
        self.radioA.select()
        self.radioB = Radiobutton(self.frameRadios, text="Adicionar ao final", variable=self.posicao, value=2)
        self.radioB.pack(side=LEFT)

        # Play
        self.btPlay = Button(self.frameText, text="Gravar", command=self.modifyFiles)
        self.btPlay.pack(fill='x')

    def setPath(self):
        """ Pergunta ao usuário a pasta que será modificada e salva o caminho na variável 'path'. """
        self.path = filedialog.askdirectory(title="Selecione a pasta onde os arquivos estão")
        self.inputPath.delete(0, END)
        self.inputPath.insert(0, self.path)
        self.setFilesName()

    def setFilesName(self):
        """ Cria uma lista com os arquivos que estão na pasta na pasta. """
        self.files = os.listdir(self.path)

    def getText(self):
        """ Pega o texto digitado no areaText e armazena em uma variável. """
        self.text = self.areaText.get("0.0", END)

    def clearText(self):
        """ Limpa o conteúdo do areaText """
        self.areaText.delete("0.0", END)

    def modifyFiles(self):
        """ Modifica todos os arquivos em self.files e adiciona o que está no self.text """
        self.getText()
        for file in self.files:
            fileOpen = open(self.path + '/' + file, "r+")
            content = fileOpen.readlines()
            posicao = 0 if self.posicao == 1 else len(content)
            content.insert(posicao, self.text)
            fileOpen.seek(0,0)
            fileOpen.writelines(content)
            fileOpen.close()
        self.clearText()

if __name__ == '__main__':
    root = Tk()
    App(root)
    root.mainloop()
