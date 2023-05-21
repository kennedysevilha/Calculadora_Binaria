
def decimal_para_binario(decimal):
    # Converte o número decimal para binário
    return bin(decimal)[2:]

def binario_para_decimal(binario):
    # Converte o número binário para decimal
    return int(binario, 2)


print("\n\n\n Kennedy Sevilha")

while True:
    print("\n\t\t\tCalculadora Binária\n\n")

    print("Selecione o tipo de operação que deseja realizar: ")
    print("; : Conversão Decimal para Binario")
    print(". : Conversão Binario para Decimal")
    print("+ : soma")
    print("- : subtração")
    print("* : multiplicação")
    print("/ : divisão")
    print("@ : Sair")

    opcao = input("Digite a opçao desejada: ")[0]

    try:

        while not all(c in "+-*/@.;" for c in opcao):
            opcao = input("Entrada inválida! Digite uma opcao de calculo correta: ")

        if opcao == "@":
            print("Encerrando...")
            break
        
        elif opcao ==";":
            numero = int(input("Digite um numero decimal: "))
            a = decimal_para_binario(numero)
            print("\n\nResultado: ",numero,"=", a,"\n\n")
            continue

        
        num1 = input("Digite o numero: ")

        while not all(c in "01" for c in num1):
            num1 = input("Entrada inválida! Digite um número binário: ")

        if opcao ==".":
            a =  binario_para_decimal(num1)
            print("\n\nResultado: ",num1, "=", a,"\n\n")
            continue
            
        

        num2 = input("Digite o numero: ")

        while not all(c in "01" for c in num2):
            num2 = input("Entrada inválida! Digite um número binário: ")

        if opcao == "+":
            
            a = binario_para_decimal(num1)
            b = binario_para_decimal(num2)

            resultado = a+b
            print("\n\nO resultado da soma Binária é: ",decimal_para_binario(resultado),"\n\n")

        elif opcao == "-":
            
            a = binario_para_decimal(num1)
            b = binario_para_decimal(num2)

            resultado = a-b
            print("\n\nO resultado da subtração Binária é: ",decimal_para_binario(resultado),"\n\n")

        elif opcao == "*":
            
            a = binario_para_decimal(num1)
            b = binario_para_decimal(num2)

            resultado = a*b
            print("\n\nO resultado da multiplicação Binária é: ",decimal_para_binario(resultado),"\n\n")
        
        elif opcao == "/":
            try:
                resultado = bin(int(num1, 2) // int(num2, 2))[2:]
                print("\n\nO resultado da divisão Binária é: ",resultado,"\n\n")
                
            except ZeroDivisionError:
                print("Não é possível dividir por zero.")


        else:
           print("Houve algum erro      :(      tente novamente...")
            
    except ValueError:
        print("Entrada inválida! Digite apenas números binarios.")

# Autor: Kennedy Sevilha
# Data: 10/05/2023