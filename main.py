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

def menu():
    print("1 - Calcular energia do fóton absorvido/emitido")
    print("2 - Calcular frequência do fóton absorvido/emitido")
    print("3 - Calcular comprimento de onda do fóton absorvido/emitido")
    print("4 - Calcular raio da órbita")
    print("5 - Calcular velocidade")
    print("6 - Calcular energia cinética")
    print("7 - Calcular energia potencial")
    print("8 - Calcular energia total")
    print("9 - Calcular comprimento de onda do elétron")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao