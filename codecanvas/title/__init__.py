styles = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m"
}

def title(message, level=1, width=50, bold=False, style="reset"):
    """
    Exibe uma mensagem de título formatada com bordas e estilos opcionais.

    :param message: A mensagem a ser exibida como título (string).
    :param level: O nível do título, que define o tipo de borda. Valores possíveis: 1, 2, 3, ou outro valor para borda simples (padrão: 1).
    :param width: A largura total do título, incluindo bordas (int, padrão: 50).
    :param bold: Se True, aplica negrito ao título (padrão: False).
    :param style: A cor do texto, utilizando os estilos definidos em 'styles': "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white" (padrão: "reset").

    :return: Não retorna nada.
    """
    def center_text(text, width):
        return text.center(width)

    title_style = ""

    if level == 1:
        border = "#" * width
        text = center_text(f"### {message.upper()} ###", width)
    elif level == 2:
        border = "=" * width
        text = center_text(f"=== {message.upper()} ===", width)
    elif level == 3:
        border = "-" * width
        text = center_text(f"--- {message.upper()} ---", width)
    else:
        border = "-" * width
        text = center_text(message.upper(), width)

    if bold:
        title_style += styles['bold']
        
    if style != "reset":
        title_style += styles[style]

    print(f"{title_style}{border}{styles['reset']}")
    print(f"{title_style}{text}{styles['reset']}")
    print(f"{title_style}{border}{styles['reset']}")