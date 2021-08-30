def main():
    #escribe tu código abajo de esta línea
    p= float(input("Peso en kg: "))
    a= float(input("Altura en m: "))
    if p<=0 or a<=0:
        print ("Revisa tus datos, alguno de ellos es erróneo.")
    else:
        imc = p / a**2
        if imc <20 :
            print ("PESO BAJO")
        elif imc>=20 and imc<25:
            print ("NORMAL")
        elif imc >=25 and imc <30:
            print ("SOBREPESO")
        elif imc >=30 and imc <40:
            print ("OBESIDAD")
        elif imc >=40 :
            print ("OBESIDAD MORBIDA")

if __name__=='__main__':
    main()