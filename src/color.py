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


def fore(color):
    """
    Retorna o código de escape ANSI para a cor do texto especificada.

    :param color: O nome da cor do texto (string). Pode ser "black", "red", "green", "yellow", "blue", "magenta", "cyan" ou "white".
    :return: O código de escape ANSI correspondente à cor do texto especificada (string), ou uma string vazia se a cor não for encontrada.
    """
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }
    
    return colors.get(color, "")

