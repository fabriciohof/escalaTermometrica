print ("Bem vindo a Escala Termométrica em Python\n")

def switch():
    temperatura = int(input("Digite sua temperatura : "))
    print(" 1 - Celsius para Fahrenheit \n 2 - Celsius para Kelvin\n 3 - Fahrenheit para Celsius \n"
          " 4 - Fahrenheit para Kelvin\n 5 - Kelvin para Celsius\n 6 - Kelvin para Fahrenheit\n")

    opcao= int(input("Escolha sua Opção : "))

    if opcao == 1:
        celsius_fahrenheit = temperatura * 1.8 + 32
        print(f'{temperatura} °C em Fahrenheit é : {celsius_fahrenheit} °F' )

    elif opcao == 2:
        celsius_kelvin = temperatura + 273
        print(f'{temperatura} °C em Kelvin é : {celsius_kelvin} K')

    elif opcao == 3:
        fahrenheit_celsius = (temperatura-32)/ 1.8
        print(f'{temperatura} °F  em Celsius é : {fahrenheit_celsius} °C')

    elif opcao == 4:
        fahrenheit_kelvin = (temperatura-32)* 5/9 + 273
        print(f'{temperatura} °F  em Kelvin é : {fahrenheit_kelvin} K')

    elif opcao == 5:
        kelvin_celsius = temperatura - 273
        print(f'{temperatura} K  em Celsius é : {kelvin_celsius} °C')

    elif opcao == 6:
        kelvin_fahrenheit = (temperatura - 273) * 1.8 +32
        print(f'{temperatura} K  em Fahrenheit é : {kelvin_fahrenheit} °F')

    else:
        print("Essa opção não existe")


switch()


