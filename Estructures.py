contador= 1
NumAlum2=4
   
Superior_A_7=[]
Superior_A_8=[]

while contador < NumAlum2:
    Nom= (input("Quin es el teu nom? "))
    Cognom= (input("Quin es el teu cognom? "))
    Edat= (input("Quina es la teva edad? "))
    Nota1= int(input("Quina es la teva primera nota? "))
    Nota2= int(input("Quina es la teva segona nota? "))
    Nota3= int(input("Quina es la teva tercera nota? "))

    alumno= (Nom, Cognom, Edat, Nota1, Nota2, Nota3)

    NotaFinal1 = (Nota1 *0.3)
    NotaFinal2 = (Nota2 * 0.4)
    NotaFinal3 = (Nota3 * 0.4)

    NotaFinal = NotaFinal1 + NotaFinal2 + NotaFinal3

    if NotaFinal > 7:
        Superior_A_7.append(alumno)
        if Nota1 or Nota2 or Nota3 >= 8:
            Superior_A_8.append(alumno)
    
    contador = contador + 1

print("La nota media es igual o mayor a un 7:")
for alumno in Superior_A_7:
    print("\t", "Nom:", alumno[0],"\n" , "\t", "Cognom:", alumno[1], "\n","\t", "Edad:", alumno[2], "\n", "\t", "Nota1:", alumno[3], "\n", "\t", "Nota2:", alumno[4], "\n", "\t", "Nota3:", alumno[5], "\n",)

print("Saca un 8 o mas en cada nota:")
for alumno1 in Superior_A_8:
    print("\t", "Nom:", alumno1[0],"\n" , "\t", "Cognom:",alumno1[1], "\n","\t", "Edad:",alumno1[2], "\n", "\t", "Nota1:",alumno1[3], "\n", "\t", "Nota2:",alumno1[4], "\n", "\t", "Nota3:",alumno1[5], "\n",)
