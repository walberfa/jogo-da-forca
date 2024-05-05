"""Jogo da forca."""

from banco_palavras import escolher_palavra
from desenhar_boneco import desenhar_boneco


def jogar_forca():
    """
    Execução do jogo.
    Captura as tentativas do jogador e mostra o resultado.
    """
    palavra = escolher_palavra()
    letras_digitadas = set()
    tentativas_restantes = 6

    while True:
        print("Palavra:", "".join(letra if letra in letras_digitadas else "_" for letra in palavra))
        letra = input("Digite uma letra: ")

        if letra in letras_digitadas:
            print("Você já digitou essa letra. Tente novamente.")
            continue

        letras_digitadas.add(letra)

        if letra in palavra:
            print("Acertou!")
            if all(letra in letras_digitadas for letra in palavra):
                print("Palavra:", palavra, "\nParabéns, você ganhou!")
                break
        else:
            tentativas_restantes -= 1
            print("Errou! Você tem", tentativas_restantes, "tentativas restantes.")
            desenhar_boneco(tentativas_restantes)
            if tentativas_restantes == 0:
                print("Game over! A palavra era", palavra)
                break


jogar_forca()
