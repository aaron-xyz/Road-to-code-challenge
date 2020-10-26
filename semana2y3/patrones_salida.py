# imprime medio cuadro izquierdo
def halfSquareLeft(squareSize):
    for i in range(squareSize, 0, -1):
        print(i*"#")

# imprimie medio cuadro derecho
def halfSquareRight(squareSize):
    for i in range(1,squareSize+1):
        print(i*"#")

# Imprime cuadrado completo
def completeSquare(squareSize):
    for i in range(1,squareSize+1):
        print(squareSize*"#")

# Imprime una linea de caracteres
def lineOfChars(size):
    print(size*"#")

# imprime en cuenta regresiva
def printCountdown(number):
    for i in range(number, 0, -1):
        print(i)

# imprime un triagulo
def printTriangle(midBase):
    halfSquareRight(midBase)
    halfSquareLeft(midBase-1)


if __name__ == "__main__":
    squareSize = 5
    number = 10
    halfSquareLeft(squareSize)
    print(10*"-")
    halfSquareRight(squareSize)
    print(10*"-")
    completeSquare(squareSize)
    print(10*"-")
    lineOfChars(squareSize)
    print(10*"-")
    printCountdown(number)
    print(10*"-")
    printTriangle(squareSize)
