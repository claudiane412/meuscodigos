def compra():
    
    compras= int(input("Quantos livros você comprou?\n"))
    if compras ==0:
        pontos= 0
        print("você não tem pontos !!!")
    if compras ==1:
        pontos=5
        print("você ganhou 5 pontos")
    if compras ==2:
        pontos= 15
        print("você ganhou 15 pontos!!!","total de pontos acumulados:15 pontos\n")
    if compras ==3:
        pontos=30
        print("Você ganhou 30 pontos!!","total de pontosacumulados:30 pontos \n")
    if compras >= 4:
        pontos=60
        print("Você ganhou 60 pontos!!!!","total de pontos acumulados:60 pontos \n")
    if compras ==5:
        print("Saindooo!!!")

def pontos():
    if pontos >=20 and pontos <=30:
        print("Brinde:Uma EcoBag ou caneta personalizada!!!")
    if pontos >35 and pontos <=60:
        print("Brinde:Um livro com valor máximo de R$30,00 ou uma luminária de cabeceira!!!")
    if pontos >65:
        print("Brinde:2 livros com valor máximo de R$100,00 ou PowerBank")
    else:
        print("ponto insuficente!!!")    



