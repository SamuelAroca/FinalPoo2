class Palindromo:
    #By Samuel Aroca

    def palindromo(word):
    
        if str(word) == "".join(reversed(word)) :
            print("Es Palindromo")
        else:
            print("No es Palindromo")

    def capicua(word):
    
        if str(word) == "".join(reversed(word)) :
            print("Es Capicua")
        else:
            print("No es Capicua")    

    salir = 1

    while salir != 0:
        

        print("1 Para palindromo, 2 Para capicua")

        opc = int(input("Digite su opcion: "))            

        if opc == 1:
            n = str(input("Digite su palabra: "))
            print(palindromo(n))

        elif opc == 2:
            n = input("Digite su número: ")
            print(capicua(n))

        else:
            print("Digita una opcion correcta")

        salir = int(input("Si desea salir digite 0, si no cualquier otro numero: "))