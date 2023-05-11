import requests


def api_request():
    """
    Solicita uma palavra à Word API.

    Return:
         Palavra enviada pela API ou mensagem de erro na solicitação.
    """
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")

    if response.status_code == 200:
        data = response.json()
        word = data[0]
        return word

    else:
        return f"Erro na solicitação: {response.status_code}"
