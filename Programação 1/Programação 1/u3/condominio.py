ruido = input()
hora = int(input())

if ruido == "":
    print("Condomínio em paz.")
else:
    if hora > 6 and hora < 22:
        print("Condomínio em paz.")
    else:
        print("Perturbação detectada!")



