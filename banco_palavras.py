"""Banco de palavras. Lista gerada pelo ChatGPT."""
import random


def escolher_palavra():
    """Banco de palavras.

    Return:
        Palavra escolhida para o jogo.
    """
    palavras1 = ['abacate', 'abajur', 'abelha', 'abobora', 'abridor', 'abutre', 'alicante', 'amendoim',
                 'armadura', 'arvore', 'avestruz', 'babuino', 'banana', 'bandeira', 'banheiro',
                 'bateria', 'beijo', 'bicicleta', 'biquini', 'biscoito', 'bode', 'boia', 'bolacha',
                 'bolha', 'boneca', 'borboleta', 'boteco', 'botequim', 'bruxa', 'cachorro']

    palavras2 = ['cadeira', 'cafe', 'camaleao', 'camisa', 'campanha', 'caneca', 'canhao', 'canivete', 'capivara',
                 'carro', 'cebola', 'celular', 'cereja', 'chapeu', 'chinelo', 'chocolate', 'cobra',
                 'colher', 'dado', 'escola']

    return random.choice(palavras1 or palavras2)
