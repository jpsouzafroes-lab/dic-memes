meme_dict = {
    "CRINGE": "Algo vergonhoso",
    "STALKEAR": "Investigar alguém na internet",
    "VDD": "abreviação da palavra Verdade",
    "BISCOITAR": "Chamar atenção",
    "HATER": "Pessoa que critica os outros",
    "VLW": "abreviação da palavra valeu"
}

print("Bem-vindo ao dicionário!")

for i in range(5):
    a = input("Digite uma palavra em que você não entende: ")

    if a in meme_dict:
        print(meme_dict[a])
    else:
        print("Palavra não encontrada!")
