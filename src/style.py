def decoration(decoration):
    """
    Retorna o código de escape ANSI para o estilo de decoração especificado.

    :param decoration: O nome da decoração (string). Pode ser "bold" ou "underline".
    :return: O código de escape ANSI correspondente à decoração especificada (string), ou uma string vazia se a decoração não for encontrada.
    """
    styles = {
        "bold": "\033[1m",
        "underline": "\033[4m"
    }

    return styles.get(decoration, "")


def reset():
    """
    Retorna o código de escape ANSI para resetar todas as configurações de estilo e cor.

    Este código pode ser utilizado para reverter o texto do console ao estilo padrão, 
    removendo qualquer formatação aplicada anteriormente, como cores de texto, 
    cores de fundo e estilos de texto (negrito, sublinhado, etc.).

    Returns:
        str: O código de escape ANSI para resetar o estilo e cor do texto (\033[0m).
    """
    reset = "\033[0m"
    return reset
