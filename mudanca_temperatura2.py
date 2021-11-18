
def celsius(temp):
    fahr = ((temp * 9) / 5) + 32
    kel = temp + 273.15
    print(f'\033[1;34m\033[1;107m A temperatura em Fahrenheit: {fahr} °F \n'
        f'\033[1;31m A temperatura em Kelvin: {kel} K')

def fahrenheit(temp):
    cel = (temp - 32) * (5 / 9)
    kel = ((temp - 32) * (5 / 9)) + 273.15
    print(f'\033[1;34m\033[1;107m A temperatura em Celsius: {cel} °C \n'
        f'\033[1;31m A temperatura em Kelvin: {kel} K')

def kelvin(temp):
    cel = temp - 273.15
    fahr = (temp - 273.15) * (9 / 5) + 32
    print(f'\033[1;34m\033[1;107m A temperatura em Celsius: {cel} °C \n'
        f'\033[1;31m A temperatura em Fahrenheit: {fahr} °F')

def conversion():
    temp = float(input('''Digite o valor da sua temperatura: '''))

    unit = int(input('''
    Diga qual unidade de medida está a sua temperatura!
        1 - Celsius
        2 - Fahrenheit
        3 - Kelvin
        :'''))

    if unit == 1:
        celsius(temp)
    elif unit == 2:
        fahrenheit(temp)
    elif unit == 3:
        kelvin(temp)
    else:
        print('\033[1;31m Número inválido!')

def main():
    conversion()

main()
