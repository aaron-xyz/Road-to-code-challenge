# Hace la operacion entre 2 numeros de acuerdo al signo que hay entre ellos
def basicComputation(number1, symbol, number2):
    if (symbol == "+"):
        return number1 + number2
    elif symbol == "-":
        return number1 - number2
    elif symbol == "x" or symbol == "*":
        return number1*number2
    elif symbol == "/":
        return number1/number2
    else:
        print("Ingresa un simbolo valido [+, -, *, /]")
    return 0

if __name__ == '__main__':
    number1 = int(input("Ingresa el primer numero: "))
    number2 = int(input("ingresa el segundo numero: "))
    operation = input("Ingresa la operacion que quieres realizar: ")

    print(basicComputation(number1, operation, number2))