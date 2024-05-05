# Banco de palavras. Lista gerada pelo ChatGPT.
import random


def escolher_palavra():
    """Banco de palavras.
    Lista gerada pelo ChatGPT.

    Return:
        Palavra escolhida para o jogo.
    """
    palavras = ['abacate', 'abajur', 'abelha', 'abobora', 'abridor', 'abutre', 'alicante', 'amendoim',
                'armadura', 'arvore', 'avestruz', 'babuino', 'banana', 'bandeira', 'banheiro',
                'bateria', 'beijo', 'bicicleta', 'biquini', 'biscoito', 'bode', 'boia', 'bolacha',
                'bolha', 'boneca', 'borboleta', 'boteco', 'botequim', 'bruxa', 'cachorro',
                'cadeira', 'cafe', 'camaleao', 'camisa', 'campanha', 'caneca', 'canhao', 'canivete', 'capivara',
                'carro', 'cebola', 'celular', 'cereja', 'chapeu', 'chinelo', 'chocolate', 'cobra',
                'colher', 'dado', 'escola']

    return random.choice(palavras)
