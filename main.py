# pip install PySimpleGUI

import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome'), sg.Input()], #Primeiro Campo da Jnela
            [sg.Text('Idade'), sg.Input()], #Segundo Campo da Janela
            [sg.Button('Enviar Dados')] #Bottão para Enviar os Dados
        ]
        # Janela
        janela = sg.Window('Dados do Usuário').layout(layout) #Cabeçalho da Janela

        # Extrair os dados da Janela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()
