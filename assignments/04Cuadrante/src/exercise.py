def main():
    # Escribe tu código abajo de esta línea
    g= int(input("Introduce los grados: "))
    if (g < 0) or (g > 360)  :
        print ("excede")
    elif (g % 90)==0:
        print("eje")
    elif (90 > g > 0):
        print("cuadrante 1")
    elif (180 > g > 90):
        print("cuadrante 2")
    elif (270 > g > 90):
        print("cuadrante 3")
    elif (360 > g > 270): 
        print("cuadrante 4")

if __name__ == '__main__':
    main()
