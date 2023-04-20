def desenhar_boneco(tentativas_restantes):
    """Desenho dos bonecos a cada tentativa."""
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
