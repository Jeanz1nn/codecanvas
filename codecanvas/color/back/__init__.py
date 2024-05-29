def back(color):
    """
    Retorna o código de escape ANSI para a cor de fundo especificada.

    :param color: O nome da cor de fundo (string). Pode ser "black", "red", "green", "yellow", "blue", "magenta", "cyan" ou "white".
    :return: O código de escape ANSI correspondente à cor de fundo especificada (string), ou uma string vazia se a cor não for encontrada.
    """
    colors = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m"
    }
    
    return colors.get(color, "")
