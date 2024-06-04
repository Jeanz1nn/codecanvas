styles = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "fg_black": "\033[30m",
    "fg_red": "\033[31m",
    "fg_green": "\033[32m",
    "fg_yellow": "\033[33m",
    "fg_blue": "\033[34m",
    "fg_magenta": "\033[35m",
    "fg_cyan": "\033[36m",
    "fg_white": "\033[37m",
    "bg_black": "\033[40m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m"
}

def text(message, align="left", width=0, bold=False, underline=False, transform="", fore_color="reset", back_color="reset"):
    """
    Exibe uma mensagem de texto altamente personalizável.

    :param message: A mensagem a ser exibida (string).
    :param align: Alinhamento do texto: "left", "right", "center" (padrão: "left").
    :param width: Largura total do texto alinhado (int, padrão: 0).
    :param bold: Se True, aplica negrito ao texto (padrão: False).
    :param underline: Se True, sublinha o texto (padrão: False).
    :param transform: Transforma o texto: "upper", "capitalize", "lower" (padrão: "").
    :param fore_color: Cor do texto: "fg_black", "fg_red", "fg_green", "fg_yellow", "fg_blue", "fg_cyan", "fg_magenta", "fg_white" (padrão: "reset").
    :param back_color: Cor do fundo do texto: "bg_black", "bg_red", "bg_green", "bg_yellow", "bg_blue", "bg_cyan", "bg_magenta", "bg_white" (padrão: "reset").

    :return: Não retorna nada.
    """
    style = ""
    message_transform = message

    if bold:
        style += styles["bold"]
    if underline:
        style += styles["underline"]
    if fore_color != "reset":
        style += styles[fore_color]
    if back_color != "reset":
        style += styles[back_color]
    if transform == "upper":
        message_transform = message.upper()
    elif transform == "lower":
        message_transform = message.lower()
    elif transform == "capitalize":
        message_transform = message.capitalize()

    styled_message = f"{style}{message_transform}{styles['reset']}"

    if align == "center":
        styled_message = styled_message.center(width)
    elif align == "left":
        styled_message = styled_message.ljust(width)
    elif align == "right":
        styled_message = styled_message.rjust(width)

    print(styled_message)
