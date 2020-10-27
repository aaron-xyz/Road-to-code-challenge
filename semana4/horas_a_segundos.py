# Convierte horas y minutos a segundos
def convertToSeconds(hours, minutes):
    return(hours*3600 + minutes*60)

if __name__ == '__main__':
    hours = int(input("Cuantas horas? "))
    minutes = int(input("Cuantos minutos? "))
    totalSeconds = convertToSeconds(hours, minutes)
    print(f"{hours} horas y {minutes} minutos equivalen a {totalSeconds} segundos.")
