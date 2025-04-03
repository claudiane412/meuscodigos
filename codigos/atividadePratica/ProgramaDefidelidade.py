def menu():
    while True:
        print("\n Programa de Fidelidade")
        print("1 - 0 livros ,0 Pontos ")
        print("2 - 1 livro,5 Pontos")
        print("3 - 2 livros,15 Pontos")
        print("4 - 3 livros,30 pontos")
        print("5- 4 ou mais livros, 60 Pontos")
        print("6- Sair")
        opcao = input ("Escolha uma opção: ")
    

        if opcao == "1":
          print("Voce não comprou livros, 0 pontos")
          break
        elif opcao == "2":
            print("Você comprou 1 livro,você ganhou 5 Pontos")
        elif opcao == "3":
            print("Você comprou 2 livros,ganhou 15 pontos")
        elif opcao == "4":
            print("Você comprou 3 livros, você ganhou 30 pontos")
        elif opcao == "5":
            print("Você comprou mais de 4 livros,você ganhou 60 pontos")
        elif opcao =="6":
            print("Saindooo!!!!")
        else:
            print("Opção Inválida!")
            break

        cliente= int(input("digite a quantidade de Pontos que você recebeu:"))
        if cliente == 0:
            print("você nao recebe brinde!!")
        if cliente >20 and 30:
            print("escolha entre A EcoBag ou a caneta personalizada!!!!")
        if cliente ==35 and 60:
            print("escolha entre um livro de no máximo R$30,00 ou uma luminária!!")
        if cliente >65:
            print("Você pode escolher entre 2 livros de no máximo R$100,00 ou uma PowerBank!!!")
            break
menu()