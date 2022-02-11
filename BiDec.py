'''
BiDec é um programa de aritmética e conver-
são binária/decimal.
Sendo possivel realizar:
cálculos entre números inteiros binários tal qual
(adição, subtração, multiplicação e divisão) e conversão entre as bases
binária e decimal.

Autor: Iriedson Souto
'''
# função que tem como parametro um numero binario e converte ele em decimal
def binDeci(num):
    numDec = 0
    V = []
    for i in range(len(num)):
        g = num[i]
        g = int(g)
        V.append(g)
    V.reverse()
    for i in range(len(V)):
        V[i] = int(V[i])
        e = V[i]*2**i
        numDec = e + numDec
    return(numDec)

# função que tem como parametro um numero decimal e converte ele em binario
def deciBin(num):
    numBi = ""
    while num != 0:
        d = num%2
        num = num//2
        numBi = numBi + str(d) 
    return(numBi[::-1])

#Exibe a mensagem introdutoria
print("""\
-----------------SEJA BEM VINDO AO BIDEC!!!------------------
--O seu programa de aritmética e conversão binária/decimal.--

ESCOLHA OQUE DESEJA REALIZAR DIGITANDO O NÚMERO EQUIVALENTE DEMONSTRADO NO MENU ABAIXO:
""")

#Dá as opções do menu geral
menu = input("1 - Converter entre as bases numéricas decimal e binária.\n2 - Utilizar a calculadora binária com: adição, subtração, multiplicação e divisão.\n3 - Encerrar programa.\n")

while menu != "3":
    if menu == "1":
        whileconver = "1"
        print("\nVocê escolheu o conversor numérico!\n")
        while whileconver == "1": #laço para o menu de converção numerica
            convert = input("Digite (1) caso você queira converter de Binário para decimal, (2) caso queira de decimal para binário ou (3) para voltar: ")
            if convert == "3": #encerra laçõ de converção
                whileconver = "3"
            else:
                if convert == "1": #converte de binario para decimal
                    num = input("\nInforme um número binário: ")      
                    print("\nSeu número em decimal é:",binDeci(num))
                elif convert == "2": #converte de decimal para binario
                    num = int(input("\nInforme um número decimal: "))
                    print("\nSeu número em binário é:",deciBin(num))

                else:
                    print("\nOpção inválida, tente novamente!\n")
                whileconver = input("\nDigite (1) caso queira realizar mais alguma conversão: ")   

    elif menu ==  "2":
        whilecalcu = "1"
        print("\nVocê escolheu a calculadora Binária!\n")
        while whilecalcu == "1": #laço para o menu de calculadora binaria
            calcu = input("Digite (1) caso você queira somar, (2) para subtrair, (3) para multiplicar, (4) para dividir ou (5) para voltar: ")
            if calcu == "5": #encerra laçõ de calculadora binaria
                whilecalcu = "5"
            else: #para calcular os numeros são convertidos em base decimal e então executa a operação, apos isso o resultado é convertido para binario e exibido
                num = binDeci(input("Informe o primeiro número binário: "))
                num2 = binDeci(input("Informe o segundo número binário: "))
                if calcu == "1":  #calcula adição      
                    num3 = num + num2
                    print("\nO resultado da soma é:",deciBin(num3))
                elif calcu == "2": #calcula subtração
                    if (num > num2):
                        num3 = num - num2
                        print("\nO resultado da subtração é:",deciBin(num3))
                    else:
                        num3 = num2 - num
                        print("\nO resultado da subtração é: -",deciBin(num3))
                elif calcu == "3": #calcula multiplicação 
                    num3 = num * num2
                    print("\nO resultado da multiplicação é:",deciBin(num3))
                elif calcu == "4": #calcula divisão
                    num3 = num // num2
                    num4 = num % num2
                    print("\nO resultado da divisão é:",deciBin(num3))
                    if num4 != 0:
                        print("\nCom resto da divisão sendo:",deciBin(num4))
                else:
                    print("\nOpção inválida, tente novamente!\n")
                whilecalcu = input("\nDigite (1) caso queira realizar mais alguma operação de calculo binário: ")
    elif menu == "3": #encerra laçõ do menu e finaliza programa
        menu = "3" 
    else: #caso a escolha das opções do menu principal não seja valida, exibe as opções novamente
        print("\nEscolha inválida, tente novamente!\n")
    print("\nESCOLHA OQUE DESEJA REALIZAR DIGITANDO O NÚMERO EQUIVALENTE DEMONSTRADO NO MENU ABAIXO:\n")
    print("1 - Converter entre as bases numéricas decimal e binária\n2 - Utilizar a calculadora binária com: adição, subtração, multiplicação e divisão\n3 - Encerrar programa")
    menu = input()
print("\nObrigado pela preferência!!! :D")
