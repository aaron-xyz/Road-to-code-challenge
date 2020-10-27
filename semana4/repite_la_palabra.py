# repite una string una N cantidad de veces usando recursividad
def repeatString(word, times):
    if times == 0:
        return ""
    else:
        return word + repeatString(word,times-1)


if __name__ == '__main__':
    word = input("Cual es la palabra? ")
    reps = int(input("Cuantas veces quieres repetirla? "))
    repetitions = repeatString(word, reps)
    print(repetitions)