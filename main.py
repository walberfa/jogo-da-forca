import random


def escolher_palavra():

    palavras = ["abacaxi", "banana", "laranja", "limao", "manga"]
    return random.choice(palavras)


def jogar_forca():

    palavra = escolher_palavra()
    letras_digitadas = set()
    tentativas_restantes = 6

    while True:
        print("Palavra:", "".join(letra if letra in letras_digitadas else "_" for letra in palavra))
        letra = input("Digite uma letra: ")

        if letra in letras_digitadas:
            print("Você já digitou essa letra. Tente novamente.")
        else:
            letras_digitadas.add(letra)
            if letra in palavra:
                print("Acertou!")
                if all(letra in letras_digitadas for letra in palavra):
                    print("Parabéns, você ganhou!")
                    break
            else:
                tentativas_restantes -= 1
                print("Errou! Você tem", tentativas_restantes, "tentativas restantes.")
                desenhar_boneco(tentativas_restantes)
                if tentativas_restantes == 0:
                    print("Game over! A palavra era", palavra)
                    break


def desenhar_boneco(tentativas_restantes):

    if tentativas_restantes == 5:
        print(""" ________
 |      |
 |      O
 |   
 |   
_|_
            """)
    elif tentativas_restantes == 4:
        print(""" ________
 |      |
 |      O
 |      |
 |    
_|_
            """)
    elif tentativas_restantes == 3:
        print(""" ________
 |      |
 |      O
 |     /|
 |     
_|_
            """)
    elif tentativas_restantes == 2:
        print(""" ________
 |      |
 |      O
 |     /|\\
 |     
_|_
                """)
    elif tentativas_restantes == 1:
        print(""" ________
 |      |
 |      O
 |     /|\\
 |     /
_|_
                """)
    elif tentativas_restantes == 0:
        print(""" ________
 |      |
 |      O
 |     /|\\
 |     / \\
_|_
                """)


jogar_forca()
