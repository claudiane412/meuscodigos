pontos =0
while True:  
    compras= int(input("Quantos livros você comprou? (digite -1 se deseja sair!!!)"))
    if compras ==-1:
        print('saindooo!!!')
        break
    
    if compras ==0:
        pontos += 0
        #rint("você não tem pontos !!!")
    elif compras ==1:
        pontos +=5
        #print("você ganhou 5 pontos")
    elif compras ==2:
        pontos += 15
        #print("você ganhou 15 pontos!!!","total de pontos acumulados:15 pontos\n")
    elif compras ==3:
        pontos +=30
        #print("Você ganhou 30 pontos!!","total de pontosacumulados:30 pontos \n")
    elif compras >= 4:
        pontos +=60
        #print("Você ganhou 60 pontos!!!!","total de pontos acumulados:60 pontos \n")

    print(pontos)    


    if pontos >= 20 and pontos <= 30:
        print("Brinde:Uma EcoBag ou caneta personalizada!!!")
    if pontos >= 35 and pontos <= 60:
        print("Brinde:Um livro com valor máximo de R$30,00 ou uma luminária de cabeceira!!!")
    if pontos >= 65:
        print("Brinde:2 livros com valor máximo de R$100,00 ou PowerBank")
    else:
        print("ponto insuficente!!!") 