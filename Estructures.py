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
    print(alumno)