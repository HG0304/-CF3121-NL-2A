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


nInicial=0
nFinal=0
frequencia=0
comprimento_de_onda=0


def menu():
    print("Qual é a sua entrada?")
    #Propriedades do Atomo de Hidrogênio
    print("1 - Número quântico (n)")
    #Emissão/Absorção de Fótons pelo Hidrogênio 
    print("2 - Número quântico (n) inicial e final")
    #Mesmas Entradas para emisão e absorção
    print("3 - Numero quântico (n) inicial e frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    print("4 - Numero quântico (n) final e frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    #Fotons
    print("5 - Frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    print("6 - Energia do fóton (Efóton), em Joule (J) ou em elétron-volt (eV)")
    
    escolha=int(input())
    if escolha == 1:
        n_H = float(input("Digite o número quântico (n): "))
        # propriedades_Atomo_H()
    elif escolha == 2:
        nInicial=int(input("Digite o número quântico inicial: "))
        nFinal=int(input("Digite o número quântico final: "))
        # Emissao_e_absorcao_de_foton_pelo_h()
    elif escolha == 3:
        print("Digite 1 para absorção e 2 para emissão de fótons pelo H")
        escolha2=int(input())
        if escolha2==1:
            nInicial=int(input("Digite o número quântico inicial: "))
            opcao=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                # calculo de nf
            else:
                comprimento_de_onda=float(input("Digite o comprimento de onda do fóton (λ): "))
                # calculo de nf
        elif escolha2==2:
            nInicial=int(input("Digite o número quântico inicial: "))
            opcao=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                 # calculo de nf
            else:
                comprimento_de_onda=float(input("Digite o comprimento de onda do fóton (λ): "))
                # calculo de nf
    elif escolha == 4:
        print("Digite 1 para absorção e 2 para emissão de fótons pelo H")
        escolha3=int(input())
        if escolha3==1:
            nFinal=int(input("Digite o número quântico inicial: "))
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                # calculo de nf
            else:
                comprimento_de_onda=float(input("Digite o comprimento de onda do fóton (λ): "))
                # calculo de nf
        elif escolha3==2:
            nInicial=int(input("Digite o número quântico inicial: "))
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                 # calculo de ni
            else:
                comprimento_de_onda=float(input("Digite o comprimento de onda do fóton (λ): "))
                # calculo de ni
        
    elif escolha == 5:
        frequencia_foton()
    elif escolha == 6:
        energia_foton()
    else:
        print("Opção inválida")
        menu()