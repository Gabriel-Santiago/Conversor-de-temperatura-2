def main():
    temp = float(input('''Digite o valor da sua temperatura: '''))

    unit = int(input('''
    Diga qual unidade de medida está a sua temperatura!
        1 - Celsius
        2 - Fahrenheit
        3 - Kelvin
        :'''))

    if unit == 1:
        fahr = ((temp * 9) / 5) + 32
        kel = temp + 273.15
        print(f'\033[1;34m\033[1;107m A temperatura em Fahrenheit: {fahr} °F \n'
              f'\033[1;31m A temperatura em Kelvin: {kel} K')

    elif unit == 2:
        cel = (temp - 32) * (5 / 9)
        kel = ((temp - 32) * (5 / 9)) + 273.15
        print(f'\033[1;34m\033[1;107m A temperatura em Celsius: {cel} °C \n'
              f'\033[1;31m A temperatura em Kelvin: {kel} K')

    elif unit == 3:
        cel = temp - 273.15
        fahr = (temp - 273.15) * (9 / 5) + 32
        print(f'\033[1;34m\033[1;107m A temperatura em Celsius: {cel} °C \n'
              f'\033[1;31m A temperatura em Fahrenheit: {fahr} °F')

    else:
        print('\033[1;31m Número inválido!')


main()
