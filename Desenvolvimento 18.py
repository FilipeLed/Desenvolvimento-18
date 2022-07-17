def aniversario():
    sair = 0
    while (sair == 0):
        Nome = input("Digite seu nome completo \n")
        Ano = int(input("Digite o ano que você nasceu \n"))
        try:
            if (Ano >= 1922) and (Ano <= 2021) and (Nome.replace(" ", "").isalpha()):
                idade = 2022 - Ano
                sair = 1
            else:
                sair = 0
                idade = 1/sair
            print(Nome)
            print(idade,'anos')
        except:
            print("Erro, tente novamente!")
        
aniversario()