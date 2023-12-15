Nom= (input("Quin es el teu nom? "))
Cognom= (input("Quin es el teu cognom? "))
Edat= (input("Quina es la teva edad? "))
Nota1= int(input("Quina es la teva primera nota? "))
Nota2= int(input("Quina es la teva segona nota? "))
Nota3= int(input("Quina es la teva tercera nota? "))

alumno= (Nom, Cognom, Edat, Nota1, Nota2, Nota3)
Superior_A_7=[]
Superior_A_8=[]

NotaFinal1 = (Nota1 *0.3)
NotaFinal2 = (Nota2 * 0.4)
NotaFinal3 = (Nota3 * 0.4)

NotaFinal = NotaFinal1 + NotaFinal2 + NotaFinal3

if NotaFinal > 7:
    Superior_A_7.append(alumno)
    if Nota1 or Nota2 or Nota3 > 8:
        Superior_A_8.append(alumno)