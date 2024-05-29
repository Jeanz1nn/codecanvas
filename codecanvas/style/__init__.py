def style(decoration):
    """
    Retorna o código de escape ANSI para o estilo de decoração especificado.

    :param decoration: O nome da decoração (string). Pode ser "reset", "bold", "underline" ou "reverse".
    :return: O código de escape ANSI correspondente à decoração especificada (string), ou uma string vazia se a decoração não for encontrada.
    """
    styles = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "underline": "\033[4m",
        "reverse": "\033[7m"
    }

    return styles.get(decoration, "")
