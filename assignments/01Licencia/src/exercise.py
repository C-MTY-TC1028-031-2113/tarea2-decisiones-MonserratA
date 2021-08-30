
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18: 
        identi= input ("¿Tienes identificación oficial?  (s/n): ")
        if identi == "s":
            print("Trámite de licencia concedido")
        elif identi == "n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")

    else:
        print("No cumples requisitos")


if __name__ == '__main__':
    main()
