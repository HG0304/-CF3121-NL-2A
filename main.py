# integrantes
# Hugo Emílio Nomura
# Pedro Henrique Satoru Lima Takahashi
# Vitor Monteiro Vianna
# Paulo Hudson

# Objetivo: Objetivo: Estudo o modelo de Bohr para o átomo de hidrogênio e quantização com programação em linguagem Python.

# Os cálculos no programa devem ser feitos com constantes com 4 algarismos significativos. Indicar a unidade de
# todos os valores de entrada e saída do programa. O usuário pode ser forçado a digitar na unidade indicada ou ter
# opção de digitar na unidade desejada ou escolher de uma lista.
# Os resultados dos cálculos devem ser exibidos com notação científica, com três algarismos significativos, para
# valores muito pequenos ou muito grandes.
# Os valores de entrada e saída do programa que serão avaliados são: número quântico (n), Energia do fóton (Efóton)
# absorvido/emitido, frequência do fóton (f) absorvido/emitido, comprimento de onda do fóton ()
# absorvido/emitido, raio da órbita (rn), velocidade (vn), energia cinética (Kn), energia potencial (Un), energia total (En)
# e comprimento de onda do elétron (n).
from math import *

c=3e8        #velocidade da luz
m=9.11e-31   #massa do eletron
h=6.626e-34  #constante de Planck
h2=4.136e-15 #constante de Planck em eV



def menu():
    print("Qual é a sua entrada?")
    #Propriedades do Atomo de Hidrogênio
    print("1 - Número quântico (n)")
    #Emissão/Absorção de Fótons pelo Hidrogênio 
    print("2 - Número quântico (n) inicial e final")
    #Mesmas Entradas para emisão e absorção
    print("3 - Numero quântico (n) final e frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    print("4 - Numero quântico (n) inicial e frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    #Fotons
    print("5 - Frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    print("6 - Energia do fóton (Efóton), em Joule (J) ou em elétron-volt (eV)")
    
    escolha=int(input())
    if escolha == 1:
        n_H = float(input("Digite o número quântico (n): "))
        Rn= n_H**2 * 5.29e-11       #Rn é o raio da órbita do eletron no atomo de hidrogenio
        Vn= 2.18e6/n_H              #Vn é a velocidade do eletron no atomo de hidrogenio
        Kn= 13.6/n_H**2             #Kn é a energia cinetica do eletron no atomo de hidrogenio
        Un= -27.2/n_H**2            #Un é a energia potencial do eletron no atomo de hidrogenio
        En= -13.6/n_H**2            #En é a energia total do eletron no atomo de hidrogenio
        λn= h/(m*Vn)                #λn é o comprimento de onda do eletron no atomo de hidrogenio
        print('Rn: {:.2e} m'.format(Rn))
        print('Vn: {:.2e} m/s'.format(Vn))
        print('Kn: {:.2e} J'.format(Kn))
        print('Un: {:.2e} J'.format(Un))
        print('En: {:.2e} J'.format(En))
        print('λn: {:.2e} m'.format(λn))

#-------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 2:
        nInicial=float(input("Digite o número quântico inicial: "))
        nFinal=float(input("Digite o número quântico final: "))
        EnInicial= -13.6/nInicial**2
        EnFinal= -13.6/nFinal**2
        if EnInicial>EnFinal:
            Efóton= abs(EnInicial-EnFinal) #Energia do fóton absorvido
        else:
            Efóton= EnFinal-EnInicial      #Energia do fóton absorvido   
        λ= h2* c/Efóton                    #Comprimento de onda do fóton
        f= Efóton/h2                       #Frequencia do fóton
        print('Ef: {:.2e} J'.format(Efóton))
        print('λ: {:.2e} m'.format(λ))
        print('f: {:.2e} Hz'.format(f))
        



#-------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 3:
        nFinal=float(input("Digite o número quântico Final: "))
        opcao1=int(input("Digite 1 para EMISAO ou 2 para ABSORCAO): "))
        #Emisao
        if opcao1==1:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EInicial=(-13.6/nFinal**2) + (h2*frequencia)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EInicial=(-13.6/nFinal**2) + ((h2*c)/λ)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)

        #Absorcao
        else:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EInicial=(-13.6/nFinal**2) - (h2*frequencia)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EInicial=(-13.6/nFinal**2) - ((h2*c)/λ)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)
        
#-------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 4:
        nInicial=float(input("Digite o número quântico Inicial: "))
        opcao1=int(input("Digite 1 para EMISAO ou 2 para ABSORCAO): "))
        #Emisao
        if opcao1==1:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EFinal=(-13.6/nInicial**2) - (h2*frequencia)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EFinal=(-13.6/nInicial**2) - ((h2*c)/λ)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)
        #Absorcao
        else:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EFinal=(-13.6/nInicial**2) + (h2*frequencia)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EFinal=(-13.6/nInicial**2) + ((h2*c)/λ)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)

#-------------------------------------------------------------------------------------------------------------------------------#
        
    elif escolha == 5:
        escolha4=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ):"))
        if escolha4 == 1:
            frequencia=float(input("Digite a frequencia do fóton (f): "))
            # calculo de En em Joule e Ev
        else:
            comprimento_de_onda=float(input("Digite o comprimento de onda do fóton (λ): "))
            # calculo de En em Joule e Ev
        

#-------------------------------------------------------------------------------------------------------------------------------#        
    elif escolha == 6:
        Escolha5=int(input("Digite 1 para energia do fóton (Efóton) em Joule (J) ou 2 para elétron-volt (eV): "))
        if Escolha5 == 1:
            Efóton=float(input("Digite a energia do fóton (Efóton) em Joule (J): "))
            # calculo de frequencia e comprimento de onda do fóton
        else:
            Efóton=float(input("Digite a energia do fóton (Efóton) em elétron-volt (eV): "))
            # calculo de frequencia e comprimento de onda do fóton
        
    else:
        print("Opção inválida")
        menu()

menu()