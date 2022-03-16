# Projeto "Chutar_número"
# Missão : Criar um programa no qual o usuário tem que tentar acertar o número correto gerado aleatoriamente entre 1 e 100.


import random
import PySimpleGUI as sg

class Chutar():


    def __init__(self):

    
        self.valor_aleatorio = 0
        self.continuar = True
        self.lista = list(range(1,101))

    def Gerar_Valor_Aleatorio(self):

        self.valor_aleatorio = random.choice(self.lista)

    def Valor_do_Usuario(self):

        self.valor_usuario = self.valores['Valor_Chute']


    def Iniciar(self):

        #layout

        layout = [
            [sg.Text('Chute um número entre 1 e 100', size = (40,0))],
            [sg.Input(size = (18,0) , key = 'Valor_Chute')],
            [sg.Button("Começar"), sg.Button("Sair")],
            [sg.Output(size = (39,10))]

        ]

        #criar janela

        self.janela = sg.Window('Acertar o número certo!',layout=layout)
        self.Gerar_Valor_Aleatorio()


        try:
            while True:

                #receber os valores
                self.evento, self.valores = self.janela.Read()

                if self.evento == "Sair" or self.evento == sg.WINDOW_CLOSED:
                    break

                #fazer algo com os valores
                if self.evento == "Começar":
                    self.Valor_do_Usuario()
                    
                    
                    

                    while self.continuar == True:

                        if int(self.valor_usuario) > 100 or int(self.valor_usuario) <= 0:
                            print("Só consideramos valores inteiros entre 1 e 100")
                            break

                        elif int(self.valor_usuario) > self.valor_aleatorio:
                            print(" O número é menor ")
                            break

                        elif int(self.valor_usuario) < self.valor_aleatorio:
                            print(" O número é maior")
                            break

                        
                        else:
                            print('Você acertou, parabéns')
                            #self.continuar == False
                            break

        
                   
        except:
            print('Por favor , Digite apenas números:')
            self.Iniciar()


Chutar().Iniciar()